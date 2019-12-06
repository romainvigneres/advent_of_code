from common import input_list_string


def part_one(input_str):
    param = {"(": 1, ")": -1}
    return sum([param.get(x, 0) for x in input_str])


def test_one():
    assert part_one("(())") == 0
    assert part_one("(((") == 3
    assert part_one(")())())") == -3


def part_two(input_str):
    floor = 0
    param = {"(": 1, ")": -1}
    for i, x in enumerate(input_str):
        floor += param.get(x, 0)
        if floor == -1:
            return i + 1


def test_two():
    assert part_two(")") == 1
    assert part_two("()())") == 5


def get_result():
    inp = input_list_string("2015", "01")[0]
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
