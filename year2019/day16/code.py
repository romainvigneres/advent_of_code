from common import input_list_string

def get_pattern(n, m):
	m += 1
	m %= 4 * n
	if m < n:
		return 0
	elif m < 2 * n:
		return 1
	elif m < 3 * n:
		return 0
	elif m < 4 * n:
		return -1

def calcul(lst, idx):
	idx += 1
	out = 0
	for i in range(len(lst)):
		out += lst[i] * get_pattern(idx, i)
	return int(str(out)[-1:])

def part_one(inp_str, phases):
    inp_lst = [int(x) for x in list(inp_str)]
    inp_len = len(inp_lst)
    for _ in range(phases):
        inp_lst = [calcul(inp_lst, i) for i in range(inp_len)]
    return ''.join([str(x) for x in inp_lst[:8]])


def test_one():
    assert part_one("12345678", 4) == "01029498"
    assert part_one("80871224585914546619083218645595", 100) == "24176176"
    assert part_one("19617804207202209144916044189917", 100) == "73745418"
    assert part_one("69317163492948606335995924319873", 100) == "52432133"


def part_two(inp_str, phases):
    offset = int(inp_str[:7])
    inp_lst = [int(x) for x in list(inp_str)]
    inp_lst = inp_lst * 10000
    inp_lst = inp_lst[offset:]

    inp_len = len(inp_lst)
    for _ in range(phases):
        s = sum(inp_lst)
        out = []
        for i in range(inp_len):
            out += [((s % 10) + 10) % 10]
            s -= inp_lst[i]
        inp_lst = out
    return ''.join([str(x) for x in inp_lst[:8]])

def get_result():
    inp = input_list_string("2019", "16")[0]
    test_one()
    print("Part one", part_one(inp, 100))
    print("Part two", part_two(inp, 100))
