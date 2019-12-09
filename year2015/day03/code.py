from common import input_list_string


def compute(inp_str):
    route = list(inp_str)
    x = 0
    y = 0
    houses = {(0, 0): 1}
    path = {"^": [0, 1], "v": [0, -1], ">": [1, 0], "<": [-1, 0]}
    for direction in route:
        a, b = path.get(direction)
        x += a
        y += b
        house = (x, y)
        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1
    return houses


def part_one(inp_str):
    return len(compute(inp_str))


def test_one():
    assert part_one(">") == 2
    assert part_one("^>v<") == 4
    assert part_one("^v^v^v^v^v") == 2


def compute_2(inp_str):
    route = list(inp_str)
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    robot = False
    houses = {(0, 0): 1}
    path = {"^": [0, 1], "v": [0, -1], ">": [1, 0], "<": [-1, 0]}
    for direction in route:
        a, b = path.get(direction)
        if robot:
            robot = False
            x2 += a
            y2 += b
            house = (x2, y2)
        else:
            x += a
            y += b
            house = (x, y)
            robot = True
        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1
    return houses


def part_two(inp_str):
    return len(compute_2(inp_str))


def test_two():
    assert part_two("^v") == 3
    assert part_two("^>v<") == 3
    assert part_two("^v^v^v^v^v") == 11


def get_result():
    inp = input_list_string("2015", "03")[0]
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part one", part_two(inp))
