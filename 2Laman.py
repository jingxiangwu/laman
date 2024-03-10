#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations


def is_laman_graph(G):
    """
    Check for Laman's conditions:
    1. G has n vertices and 2n - 3 edges.
    2. Every subset of k vertices induces a subgraph with at most 2k - 3 edges.
    """
    n = G.number_of_nodes()
    if G.number_of_edges() != 2*n - 3:
        return False
    for k in range(2, n+1):
        for sub_nodes in combinations(G.nodes(), k):
            if G.subgraph(sub_nodes).number_of_edges() > 2*k - 3:
                return False
    return True

# Generate random graphs
graphs = []
for _ in range(20):
    num_nodes = random.randint(2, 8)
    G = nx.gnm_random_graph(num_nodes, random.randint(num_nodes-1, num_nodes*2))
    graphs.append(G)

# Visualize and label the graphs
fig, axes = plt.subplots(4, 5, figsize=(20, 15))
for i, G in enumerate(graphs):
    ax = axes[i//5, i%5]
    is_laman = is_laman_graph(G)
    label = "Laman" if is_laman else "Not Laman"
    nx.draw(G, ax=ax, with_labels=True, node_size=700, 
            node_color='skyblue' if is_laman else 'lightgray')
    ax.set_title(label)
# plt.tight_layout()
plt.show()

fig.savefig("2_Laman_examples.pdf")