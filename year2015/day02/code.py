from common import input_list_string


def wrapping_surface(inp_str):
    z = [int(x) for x in inp_str.split("x")]
    z.sort(reverse=True)
    a, b, c = z
    return 3 * b * c + 2 * a * b + 2 * a * c


def part_one(inp_lst):
    return sum([wrapping_surface(x) for x in inp_lst])


def test_one():
    assert wrapping_surface("2x3x4") == 58
    assert part_one(["2x3x4", "1x1x10"]) == 101


def ribbon_length(inp_str):
    z = [int(x) for x in inp_str.split("x")]
    z.sort(reverse=True)
    a, b, c = z
    return 2 * b + 2 * c + a * b * c


def part_two(inp_lst):
    return sum([ribbon_length(x) for x in inp_lst])


def test_two():
    assert ribbon_length("2x3x4") == 34
    assert part_two(["2x3x4", "1x1x10"]) == 48


def get_result():
    inp = input_list_string("2015", "02")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
