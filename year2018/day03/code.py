import re
from common import input_list_string

regex = r"^#(\d*) @ (\d*),(\d*): (\d*)x(\d*)$"


def get_instr(text):
    return [int(x) for x in re.findall(regex, text)[0]]


def generate_cloth(max_x, max_y):
    cloth = []
    row = []
    for x in range(max_x + 1):
        row.append(".")
    for y in range(max_y + 1):
        cloth.append(row.copy())
    return cloth


def part_one(inp_lst, draw=False):
    instructions = [get_instr(x) for x in inp_lst]
    max_x = 0
    max_y = 0
    claimed_twice = 0
    for ins in instructions:
        mx = ins[1] + ins[3]
        my = ins[2] + ins[4]
        if mx > max_x:
            max_x = mx
        if my > max_y:
            max_y = my
    drawing = generate_cloth(max_x, max_y)
    for i, xa, ya, dx, dy in instructions:
        for y in range(ya, ya + dy):
            for x in range(xa, xa + dx):
                if drawing[y][x] == ".":
                    drawing[y][x] = str(i)
                elif drawing[y][x] != "X":
                    drawing[y][x] = "X"
                    claimed_twice += 1
    if draw:
        for row in drawing:
            print("".join(row))
    return claimed_twice


def test_one():
    test_str = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    part_one(test_str, True)


def part_two(inp_lst):
    instructions = [get_instr(x) for x in inp_lst]
    max_x = 0
    max_y = 0
    claims = []
    for ins in instructions:
        mx = ins[1] + ins[3]
        my = ins[2] + ins[4]
        if mx > max_x:
            max_x = mx
        if my > max_y:
            max_y = my
    drawing = generate_cloth(max_x, max_y)
    for i, xa, ya, dx, dy in instructions:
        claims.append(str(i))
        for y in range(ya, ya + dy):
            for x in range(xa, xa + dx):
                if drawing[y][x] == ".":
                    drawing[y][x] = str(i)
                else:
                    if str(i) in claims:
                        claims.remove(str(i))
                    if drawing[y][x] != "X":
                        if drawing[y][x] in claims:
                            claims.remove(drawing[y][x])
                        drawing[y][x] = "X"
    return claims[0]


def test_two():
    test_str = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    assert part_two(test_str) == "3"


def get_result():
    inp = input_list_string("2018", "03")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
