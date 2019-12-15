from common import input_list_string


def make_grid(size):
    grid = []
    row = []
    for x in range(size):
        row.append(0)
    for y in range(size):
        grid.append(row.copy())
    return grid


def update_grid(grid, A, B, val):
    for y in range(A[1], B[1]+1):
        for x in range(A[0], B[0]+1):
            if val in [0, 1]:
                grid[y][x] = val
            else:
                grid[y][x] = (grid[y][x] + 1) % 2


def update_grid_two(grid, A, B, val):
    for y in range(A[1], B[1]+1):
        for x in range(A[0], B[0]+1):
            if val == 0 and grid[y][x] > 0:
                grid[y][x] -= 1
            elif val > 0:
                grid[y][x] += val


def lit(grid):
    return sum([sum(x) for x in grid])


def translate(line_in):
    line_out = line_in.replace("through ", "").replace(
        "turn on", "1").replace("toggle", "2").replace("turn off", "0")
    ins, a, b = line_out.split(" ")
    ins = int(ins)
    x_a, y_a = [int(x) for x in a.split(",")]
    x_b, y_b = [int(x) for x in b.split(",")]
    return (x_a, y_a), (x_b, y_b), ins


def part_one(inp_list):
    grid_one = make_grid(1000)
    for l in inp_list:
        A, B, ins = translate(l)
        update_grid(grid_one, A, B, ins)
    return lit(grid_one)


def test_one():
    test_grid = make_grid(1000)
    assert lit(test_grid) == 0
    update_grid(test_grid, (0, 0), (999, 999), 1)
    assert(lit(test_grid)) == 1000000
    update_grid(test_grid, (0, 0), (999, 0), 2)
    assert(lit(test_grid)) == 999000
    update_grid(test_grid, (499, 499), (500, 500), 0)
    assert(lit(test_grid)) == 998996


def part_two(inp_list):
    grid_one = make_grid(1000)
    for l in inp_list:
        A, B, ins = translate(l)
        update_grid_two(grid_one, A, B, ins)
    return lit(grid_one)


def get_result():
    inp = input_list_string("2015", "06")
    test_one()
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
