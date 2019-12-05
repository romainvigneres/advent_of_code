from common import input_list_string


def intcode_computer(program_int):
    x = 0
    while x < len(program_int) - 3:
        opcode = program_int[x]
        a = program_int[program_int[x + 1]]
        b = program_int[program_int[x + 2]]
        pos = program_int[x + 3]
        x += 4
        if opcode == 1:
            program_int[pos] = a + b
        elif opcode == 2:
            program_int[pos] = a * b
        elif opcode == 99:
            break
    return program_int[0]


def test_one():
    assert intcode_computer([1, 0, 0, 0, 99]) == 2
    assert intcode_computer([2, 3, 0, 3, 99]) == 2
    assert intcode_computer([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30


def get_result():
    inp = input_list_string("year2019/day02/input.txt")
    program = [int(x) for x in inp[0].split(",")]
    program2 = program.copy()
    # part one
    test_one()
    program[1] = 12
    program[2] = 2
    print("Part one", intcode_computer(program))
    # part2
    exit = False
    for noun in range(0, 100):
        for verb in range(0, 100):
            pro = program2.copy()
            pro[1] = noun
            pro[2] = verb
            if intcode_computer(pro) == 19690720:
                print("Part two", 100 * noun + verb)
                exit = True
                break
        if exit:
            break
