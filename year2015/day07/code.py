from common import input_list_string


def calculate(name, results, calc):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0], results, calc)
        else:
            op = ops[-2]
            if op == "AND":
                res = calculate(ops[0], results, calc) & calculate(
                    ops[2], results, calc
                )
            elif op == "OR":
                res = calculate(ops[0], results, calc) | calculate(
                    ops[2], results, calc
                )
            elif op == "NOT":
                res = ~calculate(ops[1], results, calc) & 0xFFFF
            elif op == "RSHIFT":
                res = calculate(ops[0], results, calc) >> calculate(
                    ops[2], results, calc
                )
            elif op == "LSHIFT":
                res = calculate(ops[0], results, calc) << calculate(
                    ops[2], results, calc
                )
        results[name] = res
    return results[name]


def part_one(inp_lst):
    calc = dict()
    results = dict()
    for command in inp_lst:
        (ops, res) = command.split("->")
        calc[res.strip()] = ops.strip().split(" ")
    return calculate("a", results, calc)


def part_two(inp_lst):
    calc = dict()
    results = dict()
    for command in inp_lst:
        (ops, res) = command.split("->")
        calc[res.strip()] = ops.strip().split(" ")
    new_res = {"b": calculate("a", results, calc)}
    return calculate("a", new_res, calc)


def get_result():
    inp = input_list_string("2015", "07")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))
