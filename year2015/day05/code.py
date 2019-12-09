from common import input_list_string

VOWELS = ["a", "e", "i", "o", "u"]
ILLEGAL = ["ab", "cd", "pq", "xy"]


def compute(inp_str):
    if sum([list(inp_str).count(x) for x in VOWELS]) < 3:
        return False
    for i in ILLEGAL:
        if i in inp_str:
            return False
    for x in range(len(inp_str) - 1):
        if inp_str[x] == inp_str[x + 1]:
            return True
    return False


def part_one(inp_lst):
    return sum([1 for x in inp_lst if compute(x)])


def test_one():
    assert compute("ugknbfddgicrmopn") == True
    assert compute("aaa") == True
    assert compute("jchzalrnumimnmhp") == False
    assert compute("haegwjzuvuyypxyu") == False
    assert compute("dvszwmarrgswjxmb") == False


def has_disjoint_pair(inp_str):
    for x in range(len(inp_str) - 1):
        st = inp_str[x : x + 2]
        rest = inp_str[x + 2 :]
        if st in rest:
            return True
    return False


def has_xyx(inp_str):
    for y in range(len(inp_str) - 2):
        if inp_str[y] == inp_str[y + 2]:
            return True
    return False


def compute_2(inp_str):
    return has_disjoint_pair(inp_str) and has_xyx(inp_str)


def part_two(inp_lst):
    return sum([1 for x in inp_lst if compute_2(x)])


def test_two():
    assert compute_2("qjhvhtzxzqqjkmpb") == True
    assert compute_2("xxyxx") == True
    assert compute_2("uurcxstgmygtbstg") == False
    assert compute_2("ieodomkazucvgmuy") == False


def get_result():
    inp = input_list_string("2015", "05")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
