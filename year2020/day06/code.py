from common import input_list_string

def part_one(inp_lst):
    out = 0
    group = ""
    for line in inp_lst:
        if line == "":
            out += len(set(group))
            group = ""
            continue
        group += line
    return out


def part_two(inp_lst):
    out = 0
    group = []
    for line in inp_lst:
        if line == "":
            inter = group.pop(0)
            for line in group:
                inter = inter.intersection(line)
            out += len(inter)
            group = []
            continue
        group.append(set(line))
    return out


def test():
    inp_tst = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
        "",
    ]
    assert part_one(inp_tst) == 11
    assert part_two(inp_tst) == 6


def get_result():
    inp = input_list_string("2020", "06")
    test()
    print(part_one(inp))
    print(part_two(inp))
