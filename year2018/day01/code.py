from common import input_list_integer

def part_one(inp_lst):
    return sum(inp_lst)

def part_two(inp_lst):
    frequencies = [0]
    freq = 0
    while True:
        for change in inp_lst:
            freq += change
            if freq not in frequencies:
                frequencies.append(freq)
            else:
                return freq

def get_result():
    inp = input_list_integer("2018", "01")
    print("Part one", part_one(inp))
    print("Part two", part_two(inp))