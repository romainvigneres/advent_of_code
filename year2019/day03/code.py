from common import input_list_string


def program(inp_list):
    wires = [i.split(",") for i in inp_list]
    wires = [[(i[0], int(i[1:])) for i in w] for w in wires]
    board = [{} for i in range(len(wires))]
    for w in range(0, len(wires)):
        board[w] = {}
        x = 0
        y = 0
        l = 0
        for wire in wires[w]:
            inc = (0, 0)
            if wire[0] == "L":
                inc = (-1, 0)
            elif wire[0] == "R":
                inc = (1, 0)
            elif wire[0] == "U":
                inc = (0, 1)
            else:  # 'D'
                inc = (0, -1)

            for i in range(0, wire[1]):
                l += 1
                x += inc[0]
                y += inc[1]
                if (x, y) not in board:
                    board[w][(x, y)] = l
    return board


def part_one(list_inp):
    board = program(list_inp)
    dists = []
    for k, v in board[0].items():
        if k in board[1]:
            dists.append(abs(k[0]) + abs(k[1]))
    return sorted(dists)[0]


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


def part_two(list_inp):
    board = program(list_inp)
    lens = []
    for k, v in board[0].items():
        if k in board[1]:
            lens.append(v + board[1][k])
    return sorted(lens)[0]


def test_two():
    test_inp1 = [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83",
    ]
    assert part_two(test_inp1) == 610
    test_inp2 = [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]
    assert part_two(test_inp2) == 410


def get_result():
    inp = input_list_string("2019", "03")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
