from common import input_integer_sep
from year2019.intcode_v2 import Intcode

def part_one(inp_lst):
    output = ""
    computer = Intcode(inp_lst)
    while not computer.done:
        p = computer.run_until_output()
        output += chr(p)
        print(output)
    return 0

def part_two(inp_lst):
    output = ""
    inp_lst[0] = 2
    i = [
        65,44,66,44,65,44,66,44,67,44,67,44,66,44,65,44,66,44,67,10,
        76,44,56,44,82,44,49,50,44,82,44,49,50,44,82,44,49,48,10,
        82,44,49,48,44,82,44,49,50,44,82,44,49,48,10,
        76,44,49,48,44,82,44,49,48,44,76,44,54,10,
        110, 10
    ]
    computer = Intcode(inp_lst, i)
    while not computer.done:
        p = computer.run_until_output()
        output += chr(p)
        print(output)
    return p

def get_result():
    inp = input_integer_sep("2019", "17")
    print("Part one", part_one(inp.copy()))
    print("Part two", part_two(inp.copy()))
