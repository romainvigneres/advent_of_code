from common import input_integer_sep
from year2019.intcode_v2 import Intcode


def part_one(inp_lst):
    # just draw the map
    output = "\n"
    computer = Intcode(inp_lst)
    while not computer.done:
        output += chr(computer.run_until_output())
    return output


def part_two(inp_lst):
    inp_lst[0] = 2
    # A,B,A,B,C,C,B,A,B,C
    # A: [L8, R12, R12, R10]
    # B: [R10, R12, R10]
    # C: [L10, R10, L6]
    i = [
        65, 44, 66, 44, 65, 44, 66, 44, 67, 44, 67, 44, 66, 44, 65, 44, 66, 44, 67, 10,
        76, 44, 56, 44, 82, 44, 49, 50, 44, 82, 44, 49, 50, 44, 82, 44, 49, 48, 10,
        82, 44, 49, 48, 44, 82, 44, 49, 50, 44, 82, 44, 49, 48, 10,
        76, 44, 49, 48, 44, 82, 44, 49, 48, 44, 76, 44, 54, 10,
        110, 10
    ]
    computer = Intcode(inp_lst, i)
    while not computer.done:
        out = computer.run_until_output()
    return out


def get_result():
    inp = input_integer_sep("2019", "17")
    print("Part one", part_one(inp.copy()))
    print("Part two", part_two(inp.copy()))
