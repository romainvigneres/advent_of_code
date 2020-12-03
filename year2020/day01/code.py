from common import input_list_integer

def get_complete_three(lst_in):
    for x in range(len(lst_in)):
        nb = lst_in[x]
        res = get_complete(lst_in, 2020-nb, x)
        if res:
            return nb * res
    return None

def get_complete(lst_in, total=2020, ignore=-1):
    for x in range(len(lst_in)):
        if x == ignore:
            continue
        nb_a = lst_in[x]
        nb_b = total - nb_a
        for y in range(len(lst_in)):
            if x == y or y == ignore:
                continue
            if lst_in[y] == nb_b:
                return nb_a * nb_b
    return None

def test_one():
    inp_tst = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    assert get_complete(inp_tst) == 514579
    assert get_complete_three(inp_tst) == 241861950

def get_result():
    inp = input_list_integer("2020", "01")
    test_one()
    print(get_complete(inp))
    print(get_complete_three(inp))