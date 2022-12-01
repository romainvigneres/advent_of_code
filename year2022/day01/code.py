from common import input_list_string

def make_lst_elf(lst):
    lst_elf = list()
    x = 0
    for cal in lst:
        if cal == "":
            lst_elf.append(x)
            x = 0
        else:
            x += int(cal)
    return lst_elf

def get_part_one(lst):
    return max(make_lst_elf(lst))

def get_part_two(lst):
    ls_elf = make_lst_elf(lst)
    ls_elf.sort(reverse=True)
    return sum(ls_elf[0:3])


def test():
    lst_tst = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
        "",
    ]
    assert get_part_one(lst_tst) == 24000
    assert get_part_two(lst_tst) == 45000

def get_result():
    inp = input_list_string("2022", "01")
    test()
    print(get_part_one(inp))
    print(get_part_two(inp))
   
