def convert_to_lst(inp_str):
    return [ord(x) for x in list(inp_str)]


def convert_to_char(inp_lst):
    return "".join([chr(x) for x in inp_lst])


def increment(lst):
    lst.reverse()
    i = 0
    while i < len(lst):
        if lst[i] < 122:
            lst[i] += 1
            break
        else:
            lst[i] = 97
            i += 1
    lst.reverse()


def first_req(lst):
    i = 0
    while i < len(lst) - 2:
        if lst[i] + 1 == lst[i + 1] and lst[i + 1] + 1 == lst[i + 2]:
            return True
        i += 1
    return False


def second_req(lst):
    if 105 in lst:
        return False
    elif 108 in lst:
        return False
    elif 111 in lst:
        return False
    else:
        return True


def third_req(lst):
    nrep = 0
    skipnext = False
    for i in range(len(lst) - 1):
        if skipnext:
            skipnext = False
            continue
        if lst[i] == lst[i + 1]:
            nrep += 1
            skipnext = True
    return nrep > 1


def part_one(inp_str):
    inp_lst = convert_to_lst(inp_str)
    while True:
        increment(inp_lst)
        if not first_req(inp_lst):
            continue
        if not second_req(inp_lst):
            continue
        if not third_req(inp_lst):
            continue
        break
    return convert_to_char(inp_lst)


def test_one():
    inp_test = "abcdffaa"
    lst_test = convert_to_lst(inp_test)
    assert first_req(lst_test) == True
    assert second_req(lst_test) == True
    assert third_req(lst_test) == True
    assert part_one("abcdefgh") == "abcdffaa"
    assert part_one("ghijklmn") == "ghjaabcc"


def get_result():
    inp_str = "vzbxkghb"
    test_one()
    print("Part one", part_one(inp_str))
    print("Part two", part_one("vzbxxyzz"))
