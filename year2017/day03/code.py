def build_map(max_int):
    plan = dict()
    z = 1
    x = 1
    y = 0
    plan[1] = [0, 0]
    if max_int == 1:
        return plan
    while True:
        zsquare = z ** 2
        step = z+1
        fin = ((z+2) ** 2) + 1
        for i in range(zsquare + 1, zsquare + step):
            plan[i] = [x, y]
            if i == max_int:
                return plan
            y += 1
        for i in range(zsquare + step, zsquare + 2 * step):
            plan[i] = [x, y]
            if i == max_int:
                return plan
            x -= 1
        for i in range(zsquare + 2 * step, zsquare + 3 * step):
            plan[i] = [x, y]
            if i == max_int:
                return plan
            y -= 1
        for i in range(zsquare + 3 * step, fin):
            plan[i] = [x, y]
            if i == max_int:
                return plan
            x += 1
        z += 2


def manhattan(map_dict, val):
    x, y = map_dict[val]
    return abs(x) + abs(y)


def part_one(inp_int):
    plan = build_map(inp_int)
    return manhattan(plan, inp_int)


def test_one():
    assert part_one(1) == 0
    assert part_one(12) == 3
    assert part_one(23) == 2
    assert part_one(1024) == 31

def adjacent(map_dict, a, b):
    xa, ya = map_dict[a]
    xb, yb = map_dict[b]
    if abs(xa-xb) <= 1 and abs(ya-yb) <= 1:
        return True
    return False

def part_two(inp_int):
    plan = build_map(inp_int)
    plan2 = {1: 1}
    for i in range(2, inp_int+1):
        value = 0
        for u in range(i-1, 0, -1):
            if adjacent(plan, i, u):
                value += plan2[u]
        if value > inp_int:
            return value
        plan2[i] = value
        

def test_two():
    assert part_two(6) == 10
    assert part_two(100) == 122
    assert part_two(300) == 304

def get_result():
    inp = 347991
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
