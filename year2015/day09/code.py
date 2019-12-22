from common import input_list_string
import networkx as nx
from itertools import permutations


def part_one(inp_lst):
    Graphtype = nx.MultiGraph()
    inp_lst = [x.replace(" to ", " ").replace(" = ", " ") for x in inp_lst]
    G = nx.read_edgelist(inp_lst, create_using=Graphtype,
                         nodetype=str, data=(('distance', float),))
    all_possible = []
    for subset in permutations(G.nodes()):
        dis = 0
        for x in range(len(subset)-1):
            dis += G.get_edge_data(subset[x], subset[x+1])[0]['distance']
        all_possible.append(dis)
    return min(all_possible)


def test_one():
    test_inp = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    assert part_one(test_inp) == 605

def part_two(inp_lst):
    Graphtype = nx.MultiGraph()
    inp_lst = [x.replace(" to ", " ").replace(" = ", " ") for x in inp_lst]
    G = nx.read_edgelist(inp_lst, create_using=Graphtype,
                         nodetype=str, data=(('distance', float),))
    all_possible = []
    for subset in permutations(G.nodes()):
        dis = 0
        for x in range(len(subset)-1):
            dis += G.get_edge_data(subset[x], subset[x+1])[0]['distance']
        all_possible.append(dis)
    return max(all_possible)

def test_two():
    test_inp = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    assert part_two(test_inp) == 982

def get_result():
    inp = input_list_string("2015", "09")
    test_one()
    print("Part one", part_one(inp))
    test_two()
    print("Part two", part_two(inp))
