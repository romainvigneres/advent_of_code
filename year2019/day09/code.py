from common import input_integer_sep
from year2019.intcode import VM as computer


def part_one(program, input_val=1):
    return computer(program, input_val).run()


def test_one():
    assert len(str(part_one([1102, 34915192, 34915192, 7, 4, 7, 99, 0]))) == 16
    assert part_one([104, 1125899906842624, 99]) == 1125899906842624


def get_result():
    inp = input_integer_sep("2019", "09")
    test_one()
    print("Part one", part_one(inp, 1))
    print("Part two", part_one(inp, 2))
