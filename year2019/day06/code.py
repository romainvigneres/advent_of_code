import networkx as nx

from common import input_list_string


def read_edgelist(inp_lst, delimiter):
    return nx.Graph([line.split(delimiter) for line in inp_lst])


def part_one(graph):
    return sum([nx.shortest_path_length(graph, node, "COM") for node in graph.nodes])


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
    g = read_edgelist(input_test, ")")
    assert part_one(g) == 42


def part_two(graph):
    return nx.shortest_path_length(graph, source="YOU", target="SAN") - 2


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
    g = read_edgelist(input_test, ")")
    assert part_two(g) == 4


def get_result():
    inp = input_list_string("2019", "06")
    graph = read_edgelist(inp, ")")
    test_one()
    print("Part one", part_one(graph))
    test_two()
    print("Part two", part_two(graph))
