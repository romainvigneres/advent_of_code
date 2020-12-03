from common import input_list_string

def clean_line(l):
    ran, let, pwd = l.split()
    m, M = [int(x) for x in ran.split("-")]
    let = let[0]
    return m, M, let, pwd

def part_one(lst_in):
    c = 0
    for li in lst_in:
        m, M, let, pwd = clean_line(li)
        val = list(pwd).count(let)
        if val >= m and val <= M:
            c += 1
    return c

def part_two(lst_in):
    c = 0
    for li in lst_in:
        y, n, let, pwd = clean_line(li)
        if (pwd[y-1] == let and pwd[n-1] != let) or (pwd[y-1] != let and pwd[n-1] == let):
            c += 1
    return c

def test():
    inp_tst = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert part_one(inp_tst) == 2
    assert part_two(inp_tst) == 1

def get_result():
    inp = input_list_string("2020", "02")
    test()
    print(part_one(inp))
    print(part_two(inp))