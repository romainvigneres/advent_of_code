from common import input_integer_sep
from year2019.intcode_v2 import Intcode

PULLED = {
    1: "#",
    0: "."
}


def part_one(program, draw=False):
    if draw:
        output = "\n"
    total = 0
    for y in range(50):
        for x in range(50):
            pull = Intcode(program.copy(), [x, y]).run_until_output()
            total += pull
            if draw:
                output += PULLED.get(pull)
        if draw:
            output += "\n"
    if draw:
        print(output)
    return total


def part_two(program):
    x, y = 0, 99
    while True:
        while not Intcode(program.copy(), [x, y]).run_until_output():
            x += 1
        if Intcode(program.copy(), [x+99, y-99]).run_until_output():
            return 10000 * x + y - 99
        y += 1


def get_result():
    inp = input_integer_sep("2019", "19")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
