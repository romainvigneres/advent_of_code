from common import input_list_integer

def get_part_one(l):
    lst = l.copy()
    prev = lst.pop(0)
    c = 0
    for x in lst:
        if x > prev:
            c += 1
        prev = x
    return c

def get_part_two(lst):
    new_lst = []
    x = 0
    while x < len(lst)-2:
        new_lst.append(lst[x]+lst[x+1]+lst[x+2])
        x += 1
    return get_part_one(new_lst)

def test_one():
    inp_test = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    assert get_part_one(inp_test) == 7
    assert get_part_two(inp_test) == 5

def get_result():
    inp = input_list_integer("2021", "01")
    test_one()
    print(get_part_one(inp))
    print(get_part_two(inp))
    
