from common import input_list_string


def part_one(inp_str):
    total_score = 0
    dep = 0
    in_garb = False
    skip = False
    for ch in inp_str:
        if in_garb:
            if skip:
                skip = False
            elif ch == "!":
                skip = True
            elif ch == ">":
                in_garb = False
        else:
            if ch == "{":
                dep += 1
            elif ch == "}":
                total_score += dep
                dep -= 1
            elif ch == "<":
                in_garb = True
    return total_score


def test_one():
    assert part_one("{}") == 1
    assert part_one("{{{}}}") == 6
    assert part_one("{{},{}}") == 5
    assert part_one("{{{},{},{{}}}}") == 16
    assert part_one("{<a>,<a>,<a>,<a>}") == 1
    assert part_one("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert part_one("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert part_one("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3


def part_two(inp_str):
    garbage_total_score = 0
    dep = 0
    in_garb = False
    skip = False
    for ch in inp_str:
        if in_garb:
            if skip:
                skip = False
            elif ch == "!":
                skip = True
            elif ch == ">":
                in_garb = False
            else:
                garbage_total_score += 1
        else:
            if ch == "{":
                dep += 1
            elif ch == "}":
                dep -= 1
            elif ch == "<":
                in_garb = True
    return garbage_total_score


def test_two():
    assert part_two("<>") == 0
    assert part_two("<random characters>") == 17
    assert part_two("<<<<>") == 3
    assert part_two("""<{o"i!a,<{i<a>""") == 10


def get_result():
    inp = input_list_string("2017", "09")[0]
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
