from common import input_list_string


def part_one(str_lst):
    double = 0
    triple = 0
    for x in str_lst:
        ls = list(x)
        ls_set = set(ls)
        d = False
        t = False
        for letter in ls_set:
            if ls.count(letter) == 2:
                d = True
            elif ls.count(letter) == 3:
                t = True
            if d and t:
                break
        if d:
            double += 1
        if t:
            triple += 1
    return double * triple


def test_one():
    input_test = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]
    assert part_one(input_test) == 12


def part_two(inp_lst):
    for i, word_a in enumerate(inp_lst):
        for j, word_b in enumerate(inp_lst):
            if i == j:
                continue
            diff = 0
            word_c = ""
            for chars in zip(list(word_a), list(word_b)):
                d = len(set(chars)) - 1
                if d == 0:
                    word_c += chars[0]
                diff += d
                if diff > 1:
                    break
            if diff == 1:
                return word_c


def test_two():
    input_test = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    assert part_two(input_test) == "fgij"


def get_result():
    inp = input_list_string("2018", "02")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
