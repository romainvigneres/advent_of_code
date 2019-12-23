from common import input_list_string
from collections import Counter


def part_one(str_lst):
    double = 0
    triple = 0
    for word in str_lst:
        ct = Counter(word).values()
        if 2 in ct:
            double += 1
        if 3 in ct:
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
                if chars[0] == chars[1]:
                    word_c += chars[0]
                    diff += 0
                else:
                    diff +=1

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
