from collections import deque
from common import input_list_string


def apply_operation(operations, addi, multi, size):
    operation = operations.popleft()
    if len(operations):
        addi, multi = apply_operation(operations, addi, multi, size)
    if operation[-2] == "cut":
        addi += int(operation[-1]) * multi
    elif operation[-1] == "stack":
        multi *= -1
        addi += multi
    else:
        multi *= pow(int(operation[-1]), -1, size)
    return addi, multi


def part_two(inp_lst):
    operations = deque(reversed([line.split(" ") for line in inp_lst]))
    position = 2020
    size = 119315717514047
    iterations = 101741582076661
    addi, multi = apply_operation(operations, 0, 1, size)
    all_multi = pow(multi, iterations, size)
    all_addi = addi * (1 - pow(multi, iterations, size)) * pow(1 - multi, -1, size)
    return (position * all_multi + all_addi) % size


def get_result():
    inp = input_list_string("2019", "22")
    print("Part two:", part_two(inp))
