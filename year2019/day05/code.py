from common import input_list_string
from year2019.intcode import intcode_computer

def get_result():
    inp = input_list_string("2019", "05")[0]
    program_int = [int(x) for x in inp.split(",")]
    print("Part one", intcode_computer(program_int, 1))
    print("Part two", intcode_computer(program_int, 5))
