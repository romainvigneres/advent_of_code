from common import input_list_string


def part_one(str_in):
    list_in = list(str_in)
    value = list_in.pop(0)
    list_in.append(value)
    total = 0
    while len(list_in) > 0:
        current = list_in.pop(0)
        if current == value:
            total += int(value)
        else:
            value = current
    return total


def test_one():
    assert part_one("1122") == 3
    assert part_one("1111") == 4
    assert part_one("1234") == 0
    assert part_one("91212129") == 9


def part_two(str_in):
    list_in = list(str_in)
    xmax = len(list_in)
    step = int(xmax / 2)
    x = 0
    total = 0
    while x < xmax:
        y = x + step
        if y >= xmax:
            y -= xmax
        if list_in[x] == list_in[y]:
            total += int(list_in[x])
        x += 1
    return total


def test_two():
    assert part_two("1212") == 6
    assert part_two("1221") == 0
    assert part_two("123425") == 4
    assert part_two("123123") == 12
    assert part_two("12131415") == 4


def get_result():
    test_one()
    day_input = input_list_string("year2017/day01/input.txt")[0]
    print("Part one", part_one(day_input))
    test_two()
    print("Part two", part_two(day_input))
