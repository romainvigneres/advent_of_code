from common import input_list_string
from itertools import permutations
from year2019.intcode import Program


def part_one(inp_str):
    code = [int(x) for x in inp_str.split(",")]
    outputs = []

    for settings in permutations(range(5)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        for amp in amps:
            output = amp.run(inputs=[output])

        outputs.append(output)

    return max(outputs)


def test_one():
    assert part_one("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0") == 43210
    assert (
        part_one(
            "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        )
        == 54321
    )
    assert (
        part_one(
            "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        )
        == 65210
    )


def part_two(inp_str):
    code = [int(x) for x in inp_str.split(",")]
    outputs = []

    for settings in permutations(range(5, 10)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        while output is not None:
            outputs.append(output)
            for amp in amps:
                output = amp.run([output])

    return max(outputs)


def test_two():
    assert (
        part_two(
            "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
        )
        == 139629729
    )


def get_result():
    inp = input_list_string("2019", "07")[0]
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
