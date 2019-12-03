from common import input_list_string


def part_one(lst_str):
    instructions = [x.split() for x in lst_str]
    register_dict = dict()
    for reg, ope, val, _, creg, sig, cval in instructions:
        if reg not in register_dict:
            register_dict[reg] = 0
        if creg not in register_dict:
            register_dict[creg] = 0
        compare = "register_dict[creg]" + sig + cval
        if eval(compare):
            if ope == "inc":
                register_dict[reg] += int(val)
            else:
                register_dict[reg] -= int(val)
    return max([v for k, v in register_dict.items()])


def test_one():
    test_input = [
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10",
    ]
    assert part_one(test_input) == 1


def part_two(lst_str):
    instructions = [x.split() for x in lst_str]
    register_dict = dict()
    max_val = 0
    for reg, ope, val, _, creg, sig, cval in instructions:
        if reg not in register_dict:
            register_dict[reg] = 0
        if creg not in register_dict:
            register_dict[creg] = 0
        compare = "register_dict[creg]" + sig + cval
        if eval(compare):
            if ope == "inc":
                register_dict[reg] += int(val)
            else:
                register_dict[reg] -= int(val)
            if register_dict[reg] > max_val:
                max_val = register_dict[reg]
    return max_val


def test_two():
    test_input = [
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10",
    ]
    assert part_two(test_input) == 10


def get_result():
    inp = input_list_string("year2017/day08/input.txt")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
