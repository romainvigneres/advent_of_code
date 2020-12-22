import re
import networkx as nx

from common import input_list_string

def countBagsIn(root, G):
    totalBags = 0
    for k, val in G[root].items():
        totalBags += val['count'] * countBagsIn(k, G) + val['count']
    return totalBags


def part_one(inp_lst, G):
    for line in inp_lst:
        m = re.match(r"(.*) bags contain (.*)$", line)
        if m:
            color = m.group(1)
            remain = m.group(2)

            for child in re.findall(r"([\d]+) (.*?) bag", remain):
                G.add_edge(color, child[1], count=int(child[0]))
    return len(nx.ancestors(G, "shiny gold"))

def part_two(inp_lst, G):
    return countBagsIn("shiny gold", G)

def test():
    inp_tst = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    G = nx.DiGraph()
    assert part_one(inp_tst, G) == 4


def get_result():
    inp = input_list_string("2020", "07")
    test()
    G = nx.DiGraph()
    print(part_one(inp, G))
    print(part_two(inp, G))
