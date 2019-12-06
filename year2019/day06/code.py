import networkx

from common import input_list_string


def read_edgelist(inp_lst, delimiter):
    G = networkx.Graph()
    for line in inp_lst:
        u, v = line.split(delimiter)
        G.add_edge(u, v)
    return G


def part_one(input_list):
    graph = read_edgelist(input_list, ")")
    orbits = 0
    for node in list(graph.nodes):
        if node != "COM":
            orbits += len(networkx.shortest_path(graph, source=node, target="COM")) - 1
    return orbits


def test_one():
    input_test = [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
    ]
    assert part_one(input_test) == 42


def part_two(input_list):
    graph = read_edgelist(input_list, ")")
    return len(networkx.shortest_path(graph, source="YOU", target="SAN")) - 3


def test_two():
    input_test = [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
        "K)YOU",
        "I)SAN",
    ]
    assert part_two(input_test) == 4


def get_result():
    inp = input_list_string("year2019/day06/input.txt")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
