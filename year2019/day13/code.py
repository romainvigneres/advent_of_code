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
    # find the ball
    for i in range(len(code)-2):
        if code[i] == 0 and code[i+1] == 3 and code[i+2] == 0:
            ball = i + 1
            break
    prog = code.copy()
    prog[0] = 2
    comp = Intcode(prog)
    # play for free
    # comp.reg[0] = 2
    for r in range(ball - 17, ball + 18):
        comp.reg[r] = 1 # fake wall
    while not comp.done:
        comp.inputs.append(0)
        x = comp.run_until_output()
        y = comp.run_until_output()
        p = comp.run_until_output()
        if x == -1 and y ==0:
            p2 = p
    return p2

def get_result():
    inp = input_integer_sep("2019", "13")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
