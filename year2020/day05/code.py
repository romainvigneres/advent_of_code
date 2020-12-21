from common import input_list_string


def binary(s):
    sl = list(s)
    sl.reverse()
    val = 0
    for i, x in enumerate(sl):
        val += (int(x) * 2 ** i)
    return val


def read_pass(inp_str):
    row = binary(inp_str[:7].replace("F", "0").replace("B", "1"))
    column = binary(inp_str[-3:].replace("L", "0").replace("R", "1"))
    return row * 8 + column


def part_one(inp_lst):
    return max([read_pass(x) for x in inp_lst])

def part_two(inp_lst):
    seats = [read_pass(x) for x in inp_lst]
    seats.sort()
    seats.pop(0)
    seats.pop(-1)
    id_min = seats[0]
    id_max = seats[-1]
    return set(range(id_min, id_max+1)) - set(seats)


def test():
    assert read_pass("BFFFBBFRRR") == 567
    assert read_pass("FFFBBBFRRR") == 119
    assert read_pass("BBFFBBFRLL") == 820
    inp_tst = [   
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]
    assert part_one(inp_tst) == 820

def get_result():
    inp = input_list_string("2020", "05")
    test()
    print(part_one(inp))
    print(part_two(inp))