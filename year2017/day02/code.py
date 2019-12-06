from common import input_list_string


def row_check(list_str):
    list_int = [int(x) for x in list_str]
    return max(list_int) - min(list_int)


def part_one(tab_str):
    return sum([row_check(x) for x in tab_str])


def test_one():
    spread = [["5", "1", "9", "5"], ["7", "5", "3"], ["2", "4", "6", "8"]]
    assert part_one(spread) == 18


def row_evenly(list_str):
    list_int = [int(x) for x in list_str]
    list_int.sort(reverse=True)
    while len(list_int) > 0:
        num = list_int.pop(0)
        x = 0
        while x < len(list_int):
            if num % list_int[x] == 0:
                return int(num / list_int[x])
            x += 1
    return 0


def part_two(tab_str):
    return sum([row_evenly(x) for x in tab_str])


def test_two():
    spread = [["5", "9", "2", "8"], ["9", "4", "7", "3"], ["3", "8", "6", "5"]]
    assert part_two(spread) == 9


def get_result():
    inp = input_list_string("2017", "02")
    spreadsheet = [x.split() for x in inp]
    test_one()
    print("Part one", part_one(spreadsheet))
    test_two()
    print("Part two", part_two(spreadsheet))
