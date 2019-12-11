from common import input_integer_sep
from year2019.intcode import intcode_computer

def get_result():
    program_int = input_integer_sep("2019", "05")
    print("Part one", intcode_computer(program_int, 1))
    print("Part two", intcode_computer(program_int, 5))
