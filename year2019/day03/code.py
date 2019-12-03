from common import input_list_string


def manhattan(coordinates):
    x, y = coordinates
    return abs(x) + abs(y)


def common_elements(list1, list2):
    return [element for element in list1 if element in list2]


def left(w, x, y, mv):
    for _ in range(mv):
        x -= 1
        w.append([x, y])
    return x, y


def right(w, x, y, mv):
    for _ in range(mv):
        x += 1
        w.append([x, y])
    return x, y


def up(w, x, y, mv):
    for _ in range(mv):
        y += 1
        w.append([x, y])
    return x, y


def down(w, x, y, mv):
    for _ in range(mv):
        y -= 1
        w.append([x, y])
    return x, y


def mvt_to_wire(lst_mvt):
    wire = []
    x = 0
    y = 0
    for mvt in lst_mvt:
        direction = mvt[0]
        move = int(mvt[1:])
        if direction == "R":
            x, y = right(wire, x, y, move)
        elif direction == "L":
            x, y = left(wire, x, y, move)
        elif direction == "U":
            x, y = up(wire, x, y, move)
        else:
            x, y = down(wire, x, y, move)
    return wire


def part_one(str_list):
    wire_a_mvmt = str_list[0].split(",")
    wire_b_mvmt = str_list[1].split(",")
    wire_a = mvt_to_wire(wire_a_mvmt)
    wire_b = mvt_to_wire(wire_b_mvmt)
    intersec = common_elements(wire_a, wire_b)
    return min([manhattan(x) for x in intersec])


def test_one():
    test_inp1 = [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83",
    ]
    assert part_one(test_inp1) == 159
    test_inp2 = [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]
    assert part_one(test_inp2) == 135
    print("tests OK")


def get_result():
    inp = input_list_string("year2019/day03/input.txt")
    test_one()
    print("Part one", part_one(inp))
