from common import input_list_string


def get_layers(inp_str, wide, tall):
    data = list(inp_str)
    layers = []
    layer_l = wide * tall
    x = 0
    while data:
        layer = []
        for _ in range(0, layer_l):
            layer.append(data.pop(0))
        layers.append(layer.copy())
    return layers

def part_one(inp_str, w, t):
    lay = get_layers(inp_str, w, t)
    x = 0
    min_0 = w * t
    ind_min = None
    while x < len(lay):
        tot = lay[x].count("0")
        if tot < min_0:
            min_0 = tot
            ind_min = x
        x += 1
    return lay[ind_min].count("1") * lay[ind_min].count("2")


def test_one():
    assert get_layers("123456789012", 3, 2) == [
        ["1", "2", "3", "4", "5", "6"], ["7", "8", "9", "0", "1", "2"]]
    assert part_one("123456789012", 3, 2) == 1

def part_two(inp_str, w, t):
    pix = {"1": "■", "0": " "}
    out_lines = [["_" for _ in range(w)] for _ in range(t)]
    for layer in get_layers(inp_str, w, t):
        x = 0
        y = 0
        for pixel in layer:
            if pixel != "2":
                if out_lines[y][x] == "_":
                    out_lines[y][x] = pix.get(pixel)
            x += 1
            if x == w:
                x = 0
                y += 1
    print_list(out_lines)

def print_list(lst):
    for row in lst:
        print('  '.join(row))

def test_two():
    part_two("0222112222120000", 2, 2)


def get_result():
    inp = input_list_string("2019", "08")[0]
    test_one()
    print("Part one", part_one(inp, 25, 6))
    test_two()
    print("Part two")
    part_two(inp, 25, 6)
