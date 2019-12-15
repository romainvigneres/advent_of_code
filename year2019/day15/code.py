from common import input_integer_sep
from year2019.intcode_v2 import Intcode
import networkx as nx
import numpy as np

mvt = [(0, 1), (0, -1), (-1, 0), (1, 0)]

direct = [1, 2, 3, 4]


def run(code):
    x = 0
    y = 0
    G = nx.Graph()
    explored = set()
    spaces = set()
    walls = set()
    point = (0, 0)
    spaces.add(point)
    G.add_node(str(point))
    comp = Intcode(code)
    oxy_node = None
    i = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    while (len(walls) + len(spaces) < (40*40 - 5)) or oxy_node is None:
        if i % 10000 == 0: 
            print(i, max_x - min_x, max_y - min_y)
        nextt = np.random.choice(direct)
        comp.inputs.append(nextt)
        p = comp.run_until_output()
        next_node = (point[0] + mvt[nextt-1][0], point[1] + mvt[nextt-1][1])
        if next_node[0] < min_x:
            min_x = next_node[0]
        elif next_node[0] > max_x:
            max_x = next_node[0]
        
        if next_node[1] < min_y:
            min_y = next_node[1]
        elif next_node[1] > max_y:
            max_y = next_node[1]

        if p == 1:
            if next_node not in spaces:
                spaces.add(next_node)
                G.add_node(str(next_node))
            G.add_edge(str(point), str(next_node))
            point = next_node
        if p == 0:
            if next_node not in walls:
                walls.add(next_node)
        if p == 2:
            if oxy_node is not None:
                i += 1
                continue
            print("Oxygen found", next_node)
            G.add_node(str(next_node))
            G.add_edge(str(point), str(next_node))
            oxy_node = next_node
        i += 1
    return G, oxy_node, spaces, walls


def get_result():
    inp = input_integer_sep("2019", "15")
    print("Part one")
    Gr, exit_node, sp, wl = run(inp)
    print(len(nx.shortest_path(Gr, source=str((0, 0)), target=str(exit_node)))-1)

    print("Part two")
    paths = []
    for x in sp:
        paths.append(len(nx.shortest_path(Gr, source=str(exit_node), target=str(x)))-1)
    print(max(paths))
