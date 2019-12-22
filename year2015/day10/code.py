def process(inp_str):
    x = 0
    st = list(inp_str)
    out = ""
    while x < len(st):
        a = st[x]
        if x == len(st)-1:
            out += f"1{a}"
            x += 1
        elif st[x + 1] != a:
            out += f"1{a}"
            x += 1
        else:
            x += 2
            y = 2
            while x < len(st) - 1:
                b = st[x]
                if a == b:
                    y += 1
                    x += 1
                else:
                    break
            out += f"{y}{a}"
    return out


def part_one(inp_str):
    out = inp_str
    for _ in range(40):
        out = process(out)
    return len(out)

def test_one():
    assert process("1") == "11"
    assert process("11") == "21"
    assert process("21") == "1211"
    assert process("1211") == "111221"
    assert process("111221") == "312211"

def part_two(inp_str):
    out = inp_str
    for _ in range(50):
        out = process(out)
    return len(out)

def get_result():
    inp = "1113122113"
    test_one()
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))