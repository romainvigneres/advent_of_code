from common import input_list_integer

def part_one(instruction):
    step = 0
    x = 0
    while True:
        if x not in range(len(instruction)):
            break

        ins = instruction[x]
        instruction[x] += 1
        x += ins
        step += 1
    return step

def test_one():
    assert part_one([0, 3, 0, 1, -3]) == 5

def part_two(instruction):
    step = 0
    x = 0
    while True:
        if x not in range(len(instruction)):
            break

        ins = instruction[x]
        if ins >=3:
            instruction[x] -= 1
        else:
            instruction[x] += 1
        x += ins
        step += 1
    return step


def test_two():
    assert part_two([0, 3, 0, 1, -3]) == 10

def get_result():
    inp = input_list_integer('year2017/day05/input.txt')
    test_one()
    print("Part one", part_one(inp.copy()))
    test_two()
    print("Part two", part_two(inp.copy()))
