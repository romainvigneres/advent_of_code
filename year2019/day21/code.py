from year2019.intcode_v2 import Intcode
from common import input_integer_sep

def part_one(inp_list):
    program1 = (
        "NOT A J\n"
        "NOT B T\n"
        "OR T J\n"
        "NOT C T\n"
        "OR T J\n"
        "AND D J\n"
        "WALK\n"
    )
    p = Intcode(
        inp_list,
        [ord(char) for char in program1]
        )
    while not p.done:
        out = p.run_until_output()
        if out > 999:
            return out


def part_two(inp_list):
    program2 = (
        "NOT C J\n"
        "NOT B T\n"
        "OR T J\n"
        "NOT A T\n"
        "OR T J\n"
        "AND D J\n"
        "NOT E T\n"
        "NOT T T\n"
        "OR H T\n"
        "AND T J\n"
        "RUN\n"
    )
    p = Intcode(
        inp_list,
        [ord(char) for char in program2]
        )
    while not p.done:
        out = p.run_until_output()
        if out > 257:
            return out

def get_result():
    inp = input_integer_sep("2019", "21")
    print("Part one", part_one(inp.copy()))
    print("Part two", part_two(inp.copy()))
