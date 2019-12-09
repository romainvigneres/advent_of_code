from hashlib import md5


def compute(inp_str, l):
    for i in range(100000000):
        if md5(f"{inp_str}{i}".encode()).hexdigest()[:l] == "0" * l:
            return i


def part_one(inp_str):
    return compute(inp_str, 5)


def test_one():
    assert part_one("abcdef") == 609043


def part_two(inp_str):
    return compute(inp_str, 6)


def get_result():
    inp = "iwrupvqb"
    test_one()
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
