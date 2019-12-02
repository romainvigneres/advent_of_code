from common import input_list_string

def compute(bank_list):
    max_bank = max(bank_list)
    bank = bank_list.index(max_bank)
    bank_list[bank] = 0
    for x in range(max_bank):
        bank_list[(bank+x+1)%len(bank_list)] += 1
    return bank_list

def part_one(int_list):
    step = 0
    states = []
    while True:
        int_list = compute(int_list)
        step += 1
        if int_list in states:
            return step
        states.append(int_list.copy())
        

def part_two(int_list):
    step = 0
    states = []
    states2 = []
    while True:
        int_list = compute(int_list)
        step += 1
        
        if int_list == states2:
            return step
        
        if int_list in states and len(states2) == 0:
            step = 0
            states2 = int_list.copy()
        states.append(int_list.copy())

def test_one():
    assert compute([0, 2, 7, 0]) == [2, 4, 1, 2]
    assert part_one([0, 2, 7, 0]) == 5

def test_two():
    assert part_two([0, 2, 7, 0]) == 4

def get_result():
    inp = input_list_string("year2017/day06/input.txt")[0].split()
    int_inp = [int(x) for x in inp]
    test_one()
    print("Part one", part_one(int_inp.copy()))
    test_two()
    print("Part two", part_two(int_inp.copy()))