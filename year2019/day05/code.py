from common import input_list_string


def op1(code, a, b, c, pos):
    code[c] = a + b
    return pos + 4


def op2(code, a, b, c, pos):
    code[c] = a * b
    return pos + 4


def op3(code, a, pos, inp):
    code[a] = inp
    return pos + 2


def op4(pos):
    return pos + 2


def op5(code, a, b, pos):
    return b if a != 0 else pos + 3


def op6(code, a, b, pos):
    return b if a == 0 else pos + 3


def op7(code, a, b, c, pos):
    code[c] = 1 if a < b else 0
    return pos + 4


def op8(code, a, b, c, pos):
    code[c] = 1 if a == b else 0
    return pos + 4


ops = [op1, op2, op3, op4, op5, op6, op7, op8]


def intcode_computer(program_inp, input_set):
    program_int = [int(x) for x in program_inp.split(",")]
    x = 0
    output = None
    while True:
        opcode = program_int[x] % 100
        a_mode = (program_int[x] % 1000) // 100
        b_mode = (program_int[x] % 10000) // 1000
        if opcode in [1, 2, 7, 8]:
            a = program_int[program_int[x + 1]] if a_mode == 0 else program_int[x + 1]
            b = program_int[program_int[x + 2]] if b_mode == 0 else program_int[x + 2]
            c = program_int[x + 3]
            x = ops[opcode - 1](program_int, a, b, c, x)
        elif opcode in [5, 6]:
            a = program_int[program_int[x + 1]] if a_mode == 0 else program_int[x + 1]
            b = program_int[program_int[x + 2]] if b_mode == 0 else program_int[x + 2]
            x = ops[opcode - 1](program_int, a, b, x)
        elif opcode == 4:
            a = program_int[program_int[x + 1]] if a_mode == 0 else program_int[x + 1]
            x = ops[3](x)
            output = a
        elif opcode == 3:
            x = ops[2](program_int, program_int[x + 1], x, input_set)
        else:
            if opcode != 99:
                print("opcode:", opcode)
            return output


def get_result():
    inp = input_list_string("2019", "05")[0]
    print("Part one", intcode_computer(inp, 1))
    print("Part two", intcode_computer(inp, 5))
