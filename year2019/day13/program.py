#!/usr/bin/env python

class Program:
    @staticmethod
    def debug(values, log=None):
        values = [int(x) for x in values.split(",")]
        variables = {}
        off = 0
        log.show(" Offset    Val Op Code        'Description'")
        while off < len(values):
            off += Program.debug_line(log, values, off, variables=variables)

    @staticmethod
    def _to_string(value):
        ret = ""
        chars = "abcdefghijklmnopqrstuvwxyz"
        while True:
            ret += chars[int(value % 26)]
            value = int(value / 26)
            if value <= 0:
                break
        return ret[::-1]

    @staticmethod
    def debug_line(log, values, off, variables=None):
        temp = Program([], 0)

        if values[off] % 100 not in temp.ops:
            log.show("{:7d} {:6d}".format(off, values[off]))
            return 1
        else:
            _func, name, params, desc = temp.ops[values[off] % 100]
            info = []
            for i in range(params):
                mode = (values[off] // [100, 1000, 10000][i]) % 10
                if mode == 1:
                    info.append(str(values[off + 1 + i]))
                elif mode == 0:
                    if variables is not None and values[off + 1 + i] >= len(values):
                        if values[off + 1 + i] not in variables:
                            variables[values[off + 1 + i]] = Program._to_string(len(variables))
                        info.append("[{}]".format(variables[values[off + 1 + i]]))
                    else:
                        info.append("[{}]".format(values[off + 1 + i]))
                elif mode == 2:
                    info.append("[{}+rel]".format(values[off + 1 + i]))
            desc = desc.format(*info)
            log.show("{:7d} {:6d} {:14s} {:30s} {}".format(
                off, 
                values[off], 
                name, 
                "'" + desc + "'", 
                ",".join([str(values[x + off]) for x in range(params + 1)]),
            ))
            return params + 1

    def __init__(self, ticker, log, debug=False):
        from collections import deque, defaultdict

        self.debug_frames = False
        self.frames = []
        self.show_debug = debug
        self.log = log
        self.ticker = defaultdict(int, [(i, ticker[i]) for i in range(len(ticker))])
        self.off = 0
        self.ops = {
            1: (self.op_add, "add", 3, "{} + {} -> {}"),
            2: (self.op_mult, "mult", 3, "{} * {} -> {}"),
            3: (self.op_input, "input", 1, "input -> {}"),
            4: (self.op_output, "output", 1, "{} -> output"),
            5: (self.op_jump_if_true, "jump_if", 2, "if {} != 0 then goto {}"),
            6: (self.op_jump_if_false, "jump_not", 2, "if {} == 0 then goto {}"),
            7: (self.op_less_than, "less_than", 3, "if {0} < {1} then 1 -> {2}, else 0 -> {2}"),
            8: (self.op_equals, "equals", 3, "if {0} == {1} then 1 -> {2}, else 0 -> {2}"),
            9: (self.op_relative, "set_relative", 1, "relative += {}"),
            99: (self.op_terminate, "terminate", 0, "exit"),
        }
        self.input = deque()
        self.output = deque()
        self.last_output = None
        self.source_output = None

        self.flag_running = True
        self.flag_input_dry = False
        self.relative = 0

    def save_frames(self):
        self.debug_frames = True

    def hook_up_output(self, source_output):
        self.source_output = source_output

    def add_to_input(self, value):
        self.input.appendleft(value)

    def tick_till_end(self):
        while self.tick():
            pass

    def tick(self):
        if self.flag_running:
            self.input_dry = False
            if self.show_debug:
                Program.debug_line(self.log, self.ticker, self.off)
            if self.debug_frames:
                self.frames.append([self.off, self.ticker.copy()])

            self.ops[self.ticker[self.off] % 100][0]()

            if self.debug_frames:
                if self.input_dry:
                    self.frames.pop(-1)
        
        return self.flag_running == True and self.input_dry == False

    def is_on_input(self):
        return self.ticker[self.off] % 100 == 3
        
    def is_on_output(self):
        return self.ticker[self.off] % 100 == 4
        
    def op_relative(self):
        self.relative += self.get_value(1)
        self.off += 2

    def op_jump_if_true(self):
        if self.get_value(1) != 0:
            self.off = self.get_value(2)
        else:
            self.off += 3

    def op_jump_if_false(self):
        if self.get_value(1) == 0:
            self.off = self.get_value(2)
        else:
            self.off += 3

    def op_less_than(self):
        if self.get_value(1) < self.get_value(2):
            self.set_value(3, 1)
        else:
            self.set_value(3, 0)
        self.off += 4

    def op_equals(self):
        if self.get_value(1) == self.get_value(2):
            self.set_value(3, 1)
        else:
            self.set_value(3, 0)
        self.off += 4

    def op_input(self):
        if self.source_output is not None:
            while len(self.source_output.output) > 0:
                self.input.appendleft(self.source_output.output.pop())

        if len(self.input) > 0:
            temp = self.input.pop()
            if self.debug_frames:
                self.frames.append(["input", temp])
            self.set_value(1, temp)
            self.off += 2
        else:
            self.input_dry = True

    def op_output(self):
        self.last_output = self.get_value(1)
        if self.debug_frames:
            self.frames.append(["output", self.last_output])
        self.output.appendleft(self.last_output)
        self.off += 2

    def op_terminate(self):
        self.off += 1
        self.flag_running = False

    def op_add(self):
        self.set_value(3, self.get_value(1) + self.get_value(2))
        self.off += 4

    def op_mult(self):
        self.set_value(3, self.get_value(1) * self.get_value(2))
        self.off += 4

    def get_value(self, index):
        mode = (self.ticker[self.off] // [0, 100, 1000, 10000][index]) % 10
        if mode == 2: # Relative
            return self.ticker[self.ticker[self.off + index] + self.relative]
        elif mode == 1: # Immediate
            return self.ticker[self.off + index]
        elif mode == 0: # Position
            return self.ticker[self.ticker[self.off + index]]
        else:
            raise Exception("Invalid get mode: " + str(mode))

    def set_value(self, index, value):
        mode = (self.ticker[self.off] // [0, 100, 1000, 10000][index]) % 10
        if mode == 2: # Relative
            self.ticker[self.ticker[self.off + index]+self.relative] = value
        elif mode == 0: # Position
            self.ticker[self.ticker[self.off + index]] = value
        else:
            raise Exception("Invalid set mode: " + str(mode))
