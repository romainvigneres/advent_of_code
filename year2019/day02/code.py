from common import input_integer_sep
from year2019.intcode import intcode_computer_v0 as intcode_computer


def part_one(program):
    return intcode_computer(program, [12, 2])


def test_one():
    assert intcode_computer([1, 0, 0, 0, 99]) == 2
    assert intcode_computer([2, 3, 0, 3, 99]) == 2
    assert intcode_computer([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30


def part_two(program):
    for noun in range(0, 100):
        for verb in range(0, 100):
            if intcode_computer(program, [noun, verb]) == 19690720:
                return 100 * noun + verb


def get_result():
    inp = input_integer_sep("2019", "02")
    test_one()
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
