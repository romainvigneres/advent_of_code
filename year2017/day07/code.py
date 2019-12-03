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

def get_data(list_input, name):
    for x in list_input:
        if x[0] == name:
            return x

class disc:
    def __init__(self, n, w, dep):
        self.name = n
        self.weight = int(w)
        self.dependencies = dep
    def total_weight(self):
        if self.dependencies is None:
            return self.weight
        return self.weight + sum([x.total_weight() for x in self.dependencies])
    def balanced(self):
        if self.dependencies is None:
            return True
        if len(set([x.total_weight() for x in self.dependencies])) == 1:
            return True
        return False

def add_to_dict(dic_obj, name, weight, dependencies, cl):
    if name in dic_obj:
        return dic_obj[name]
    if dependencies is None:
            new_obj = disc(name, weight, None)
    else:
        lst_dep = []
        for x in dependencies:
            if x in dic_obj:
                lst_dep.append(dic_obj[x])
            else:
                n, w, d = get_data(cl, x)
                lst_dep.append(add_to_dict(dic_obj, n, w, d, cl))
        new_obj = disc(name, weight, lst_dep)
    dic_obj[name] = new_obj
    return new_obj



def part_two(list_str):
    obj_dict = dict()
    clean_input = [clean_line(x) for x in list_str]
    for name, weight, dependencies in clean_input:
        if name in obj_dict:
            continue
        add_to_dict(obj_dict, name, weight, dependencies, clean_input)
    lst_unbalanced = [v for k, v in obj_dict.items() if not v.balanced()]
    for tower in lst_unbalanced:
        lst_weight = [x.total_weight() for x in tower.dependencies]
        for dis in tower.dependencies:
            if lst_weight.count(dis.total_weight()) == 1:
                faulty = dis
            else:
                normal_weight = dis.total_weight()
        diff = normal_weight - faulty.total_weight()
        return faulty.weight + diff

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
