from common import input_list_string

def clean_line(line):
    line = line.replace(" (", ";").replace(")", "").replace(" -> ", ";")
    line_lst = line.split(";")
    if len(line_lst) == 2:
        line_lst.append(None)
    else:
        line_lst[2] = line_lst[2].split(", ")
    return line_lst


def part_one(list_str):
    bottom_list = []
    dep_list = []
    clean_input = [clean_line(x) for x in list_str]
    for name, weight, dependencies in clean_input:
        if dependencies is None:
            continue
        dep_list.extend(dependencies)
        bottom_list.append(name)
    bottom = set(bottom_list) - set(dep_list)
    return list(bottom)[0]


def test_one():
    assert clean_line("pbga (66)") == ["pbga", "66", None]
    assert clean_line("fwft (72) -> ktlj, cntj, xhth") == ["fwft", "72", ["ktlj", "cntj", "xhth"]]
    input_test = [
        "pbga (66)",
        "xhth (57)",
        "ebii (61)",
        "havc (66)",
        "ktlj (57)",
        "fwft (72) -> ktlj, cntj, xhth",
        "qoyq (66)",
        "padx (45) -> pbga, havc, qoyq",
        "tknk (41) -> ugml, padx, fwft",
        "jptl (61)",
        "ugml (68) -> gyxo, ebii, jptl",
        "gyxo (61)",
        "cntj (57)"
    ]
    assert part_one(input_test) == "tknk"

def part_two(list_str):
    new_weight = 0
    bottom_list = []
    dep_list = []
    clean_input = [clean_line(x) for x in list_str]
    # TODO start from the top of the towers
    return new_weight

def test_two():
    input_test = [
        "pbga (66)",
        "xhth (57)",
        "ebii (61)",
        "havc (66)",
        "ktlj (57)",
        "fwft (72) -> ktlj, cntj, xhth",
        "qoyq (66)",
        "padx (45) -> pbga, havc, qoyq",
        "tknk (41) -> ugml, padx, fwft",
        "jptl (61)",
        "ugml (68) -> gyxo, ebii, jptl",
        "gyxo (61)",
        "cntj (57)"
    ]
    assert part_two(input_test) == 60


def get_result():
    inp = input_list_string("year2017/day07/input.txt")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
