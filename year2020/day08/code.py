from common import input_list_string

def part_one(inp_lst):
    x = 0
    accumulator = 0
    ins_done = list()
    maxx = len(inp_lst)
    while x < maxx:
        if x in ins_done:
            break
        ins_done.append(x)
        ins, val = inp_lst[x].split()
        if ins == "nop":
            x += 1
        elif ins == "jmp":
            x += int(val)
        elif ins == "acc":
            x += 1
            accumulator += int(val)
        else:
            print("Error")
            break
        continue
    return accumulator

def test_two(inp_lst, change):
    x = 0
    ins_done = list()
    maxx = len(inp_lst)
    while x < maxx:
        if x in ins_done:
            return False
        ins_done.append(x)
        ins, val = inp_lst[x].split()
        if ins == "nop" or x == change:
            x += 1
        elif ins == "jmp":
            x += int(val)
        elif ins == "acc":
            x += 1
        continue
    return True

def part_two(inp_lst):
    for i, line in enumerate(inp_lst):
        if line[0:3] == "jmp":
            if test_two(inp_lst, i):
                new_lst = inp_lst.copy()
                new_lst[i] = "nop +0"
                return part_one(new_lst)

def test():
    inp_tst = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    assert part_one(inp_tst) == 5
    assert part_two(inp_tst) == 8

def get_result():
    inp = input_list_string("2020", "08")
    test()
    print(part_one(inp))
    print(part_two(inp))