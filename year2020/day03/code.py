from common import input_list_string

def part_one(inp):
    trees = 0
    x = 0
    lenmax = len(inp[0])
    for line in inp:
        if line[x % lenmax] == "#":
            trees += 1
        x += 3
    return trees

def part_two(inp):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    maxlen = len(inp)
    lenmax = len(inp[0])
    results = 1
    for R, d in slopes:
        trees = 0
        x = 0
        y = 0
        while y < maxlen:
            if inp[y][x % lenmax] == "#":
                trees += 1
            x += R
            y += d
        results *= trees
    return results

def test():
    inp_tst = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert part_one(inp_tst) == 7
    assert part_two(inp_tst) == 336

def get_result():
    inpu = input_list_string("2020", "03")
    test()
    print(part_one(inpu))
    print(part_two(inpu))
