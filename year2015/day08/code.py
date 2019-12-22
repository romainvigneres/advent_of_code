from common import input_list_string


def part_one(inp_lst):
    return sum([len(x) - len(eval(x)) for x in inp_lst])


def part_two(inp_lst):
    return sum([2 + x.count('\\') + x.count('"') for x in inp_lst])


def get_result():
    inp = input_list_string("2015", "08")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
