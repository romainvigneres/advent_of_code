# day 02


def intcode_computer_v0(program_inp, settings=None):
    program_int = program_inp.copy()
    if settings is not None:
        program_int[1] = settings[0]
        program_int[2] = settings[1]
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
        else:
            assert opcode == 99
            return program_int[0]


# day 05


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
    program_int = program_inp.copy()
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


# day 07


class Program:
    def __init__(self, code, setting):
        self.code = code.copy()
        self.inputs = [setting]
        self.i = 0

    def get_opcode(self):
        return self.code[self.i] % 100

    def get_param(self, n):
        if self.i + n > len(self.code) - 1:
            return None

        if self.get_mode(n) == 1:
            return self.i + n
        else:
            return self.code[self.i + n]

    def get_mode(self, n):
        return self.code[self.i] // (10 ** (1 + n)) % 10

    def run(self, inputs):
        self.inputs += inputs

        while self.i < len(self.code):
            op = self.get_opcode()

            if op == 99:
                break

            p1, p2, p3 = [self.get_param(p) for p in range(1, 4)]

            if op == 1:
                self.code[p3] = self.code[p1] + self.code[p2]
                self.i += 4
            elif op == 2:
                self.code[p3] = self.code[p1] * self.code[p2]
                self.i += 4
            elif op == 3:
                self.code[p1] = self.inputs.pop(0)
                self.i += 2
            elif op == 4:
                self.i += 2
                return self.code[p1]
            elif op == 5:
                self.i = self.code[p2] if self.code[p1] != 0 else self.i + 3
            elif op == 6:
                self.i = self.code[p2] if self.code[p1] == 0 else self.i + 3
            elif op == 7:
                self.code[p3] = int(self.code[p1] < self.code[p2])
                self.i += 4
            elif op == 8:
                self.code[p3] = int(self.code[p1] == self.code[p2])
                self.i += 4
            else:
                raise Exception("Invalid opcode")


# day 09


POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MUL = 2
IN = 3
OUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADD_RELATIVE_BASE = 9
HALT = 99

READ = 0
WRITE = 1

OPS = {
    ADD: (READ, READ, WRITE),
    MUL: (READ, READ, WRITE),
    IN: (WRITE,),
    OUT: (READ,),
    JUMP_TRUE: (READ, READ),
    JUMP_FALSE: (READ, READ),
    LESS_THAN: (READ, READ, WRITE),
    EQUALS: (READ, READ, WRITE),
    ADD_RELATIVE_BASE: (READ,),
    HALT: (),
}


class VM:
    def __init__(self, code, inp):
        self.code = list(code)
        self.inp = inp

    def __getitem__(self, index):
        return self.mem[index]

    def __setitem__(self, index, val):
        self.mem[index] = val

    def get_args(self, arg_kinds, modes):
        args = [None] * 4

        for i, kind in enumerate(arg_kinds):
            a = self[self.ip + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == RELATIVE:
                a += self.relative_base

            if mode in (POSITION, RELATIVE):
                if a < 0:
                    raise Exception(f"Invalid access to negative memory index: {a}")
                elif a >= len(self.mem):
                    self.mem += [0] * (a + 1 - len(self.mem))

                if kind == READ:
                    a = self[a]
                elif kind != WRITE:
                    raise Exception(f"Invalid arg kind: {kind}")

            elif mode == IMMEDIATE:
                if kind == WRITE:
                    raise Exception(f"Invalid arg mode for write arg: {mode}")
            else:
                raise Exception(f"Invalid arg mode: {mode}")

            args[i] = a

        return args

    def run(self):
        self.ip = 0
        self.relative_base = 0
        self.mem = self.code.copy()
        out = None

        while self[self.ip] != HALT:
            instr = self[self.ip]
            op = instr % 100
            modes = instr // 100

            if op not in OPS:
                raise Exception(f"Unknown opcode: {op}")

            arg_kinds = OPS[op]
            a, b, c, d = self.get_args(arg_kinds, modes)
            self.ip += 1 + len(arg_kinds)

            if op == IN:
                self[a] = self.inp
            elif op == OUT:
                out = a
            elif op == ADD:
                self[c] = a + b
            elif op == MUL:
                self[c] = a * b
            elif op == LESS_THAN:
                self[c] = 1 if a < b else 0
            elif op == EQUALS:
                self[c] = 1 if a == b else 0
            elif op == JUMP_TRUE:
                if a != 0:
                    self.ip = b
            elif op == JUMP_FALSE:
                if a == 0:
                    self.ip = b
            elif op == ADD_RELATIVE_BASE:
                self.relative_base += a
            else:
                raise Exception(f"Unimplemented opcode: {op}")

        return out

# day 11

class Robot:
    def __init__(self, program, init_input, init_ip=0):
        self.p = program[:]
        self.i = init_input
        self.o = None  # output
        self.j = init_ip  # ip
        self.b = 0  # base for mode 2 addressing

    def write(self, addr, value):
        if addr >= len(self.p):
            self.p += [0] * (addr - len(self.p) + 10)  # add what's needed + some more
        self.p[addr] = value

    def read(self, addr):
        return addr < len(self.p) and self.p[addr] or 0  # 0 if missing addr

    def address(self, addr, mode):  # get address for 3rd operand
        if mode == 1:
            return addr
        elif mode == 2:
            return self.b + self.read(addr)
        else:
            return self.read(addr)

    def value(self, addr, mode):
        return self.read(self.address(addr, mode))

    def run(self):
        while self.read(self.j) % 100 != 99:  # run till halt
            ip = self.j
            oop = self.read(ip)
            op = oop % 100  # original and effective opcode
            self.j += (0, 4, 4, 2, 2, 3, 3, 4, 4, 2)[op]
            if op in (1, 2, 4, 5, 6, 7, 8, 9):
                v = self.value(ip + 1, (oop // 100) % 10)
            if op in (1, 2, 5, 6, 7, 8):
                w = self.value(ip + 2, (oop // 1000) % 10)
            if op in (1, 2, 7, 8):
                dest = self.address(ip + 3, (oop // 10000) % 10)
            if op == 1:
                self.write(dest, v + w)  # add
            elif op == 2:
                self.write(dest, v * w)  # mul
            elif op == 7:
                self.write(dest, int(v < w))  # setl
            elif op == 8:
                self.write(dest, int(v == w))  # sete
            elif op == 9:
                self.b += v  # rebase
            elif op == 4:
                self.o = v
                self.s = "O"
                return v  # O: yielded output
            elif op == 3:  # in
                if len(self.i) == 0:
                    self.j -= 2
                    self.s = "W"
                    return  # W: waiting input
                self.write(self.address(ip + 1, (oop // 100) % 10), self.i[0])
                self.i = self.i[1:]
            elif op == 5:  # jmpt
                if v != 0:
                    self.j = w
            elif op == 6:  # jmpf
                if v == 0:
                    self.j = w
            else:
                raise Exception("wrong opcode %d, %d at %d" % (op, oop, ip))
        self.s = "H"  # H: halt instruction

    def resume(self, data=None):  # resume after waiting input
        if data is not None:
            self.i.append(data)
        self.run()

