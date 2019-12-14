from common import input_integer_sep
from year2019.intcode_v2 import Intcode


def part_one(code):
    p1 = 0
    comp = Intcode(code.copy())
    while not comp.done:
        comp.run_until_output()
        comp.run_until_output()
        p1 += comp.run_until_output() == 2
    return p1
    
    
def part_two(code):
    p2 = 0
    ball_x = paddle_x = 0
    broken_blocks = 0
    # find the ball
    # for i in range(len(code)-2):
    #     if code[i] == 0 and code[i+1] == 3 and code[i+2] == 0:
    #         ball = i + 1
    #         break
    inp = 0
    comp = Intcode(code)
    # play for free
    comp.reg[0] = 2
    # for r in range(ball - 30, ball + 31):
    #     comp.reg[r] = 1 # fake wall
    while not comp.done:
        x = comp.run_until_output()
        y = comp.run_until_output()
        p = comp.run_until_output()
        inp = (ball_x > paddle_x) - (ball_x < paddle_x)
        comp.inputs.append(inp)
        if not comp.done:
            paddle_x = x if p == 3 else paddle_x
            ball_x = x if p == 4 else ball_x
            if p == 2:
                broken_blocks += 1
            if x == -1 and y ==0:
                p2 = p
    return p2

def get_result():
    inp = input_integer_sep("2019", "13")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
