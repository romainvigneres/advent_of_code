from common import input_list_string

def check(inp_str):
    list_str = inp_str.split()
    if len(list_str) == len(list(set(list_str))):
        return True
    return False

def part_one(list_str):
    return sum([1 for x in list_str if check(x)])

def test_one():
    assert check('aa bb cc dd ee') == True
    assert check('aa bb cc dd aa') == False
    assert check('aa bb cc dd aaa') == True

def check_two(inp_str):
    list_str = inp_str.split()
    while len(list_str) > 1:
        word = list(list_str.pop(0))
        word.sort()
        for other_word in list_str:
            if len(word) == len(other_word):
                other_word_l = list(other_word)
                other_word_l.sort()
                if word == other_word_l:
                    return False
    return True

def part_two(list_str):
    return sum([1 for x in list_str if check_two(x)])
            
def test_two():
    assert check_two('abcde fghij') == True
    assert check_two('abcde xyz ecdab') == False
    assert check_two('a ab abc abd abf abj') == True
    assert check_two('iiii oiii ooii oooi oooo') == True
    assert check_two('oiii ioii iioi iiio') == False

def get_result():
    inp = input_list_string("year2017/day04/input.txt")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))