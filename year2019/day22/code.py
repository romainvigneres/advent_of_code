from common import input_list_string


def do_ins(lst, ins):
    if ins == "deal into new stack":
        lst.reverse()
    elif "cut " in ins:
        cut = int(ins[4:])
        if cut > 0:
            for _ in range(cut):
                lst.append(lst.pop(0))
        else:
            for _ in range(abs(cut)):
                lst.insert(0, lst.pop(-1))
    elif "deal with increment " in ins:
        inc = int(ins[20:])
        m = len(lst)
        l = [0 for _ in range(m)]
        for i, x in enumerate(lst):
            l[(i * inc) % m] = x
        lst = l
    return lst


def compute(inp_deck, ins_lst):
    out_deck = inp_deck.copy()
    for ins in ins_lst:
        out_deck = do_ins(out_deck, ins)
    return out_deck


def part_one(ins_lst):
    inp_deck = [x for x in range(10007)]
    out_deck = compute(inp_deck, ins_lst)
    return out_deck.index(2019)


def test_one():
    test_deck = [x for x in range(10)]
    test_instruction = [
        "deal with increment 7",
        "deal into new stack",
        "deal into new stack",
    ]
    assert compute(test_deck, test_instruction) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    test_instruction = [
        "cut 6",
        "deal with increment 7",
        "deal into new stack",
    ]
    assert compute(test_deck, test_instruction) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    test_instruction = [
        "deal with increment 7",
        "deal with increment 9",
        "cut -2",
    ]
    assert compute(test_deck, test_instruction) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

def part_two(ins_lst):
    out_deck = [x for x in range(119315717514047)]
    for _ in range(101741582076661):
        out_deck = compute(out_deck, ins_lst)
    return out_deck[2020]

def get_result():
    inp = input_list_string("2019", "22")
    test_one()
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
