from common import input_list_integer

def part_one(inp_lst, preamble):
    x = 0
    while True:
        pre_lst = inp_lst[x:x+preamble]
        next_val = inp_lst[x+preamble]
        val_found = False
        while pre_lst:
            pr = pre_lst.pop(0)
            if next_val - pr in pre_lst:
                val_found = True
                break
        if not val_found:
            return next_val
        x += 1

def part_two(inp_lst, preamble):
    bad_number = part_one(inp_lst, preamble)
    x = 0
    while True:
        lst = [inp_lst[x], inp_lst[x+1]]
        i = 2
        while True:
            if sum(lst) < bad_number:
                lst.append(inp_lst[x+i])
                i += 1
            elif sum(lst) > bad_number:
                x += 1
                break
            else:
                return min(lst) + max(lst)

def test():
    inp_tst = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert part_one(inp_tst, 5) == 127
    assert part_two(inp_tst, 5) == 62

def get_result():
    inp = input_list_integer("2020", "09")
    test()
    print(part_one(inp, 25))
    print(part_two(inp, 25))