#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations
import sys


def is_laman_graph(G,HT):
    """
    Check for Laman's conditions:
    1. G has nV vertices and nE edges. (HT-1)* nE = HT*nV - (HT+1)
    2. Every subset of k vertices induces a subgraph with at most 2k - 3 edges.
    """
    nV = G.number_of_nodes()
    nE = G.number_of_edges()
    if  (HT-1)* nE != HT*nV - (HT+1):
        return False
    for k in range(2, nV+1):
        for sub_nodes in combinations(G.nodes(), k):
            if (HT-1)* G.subgraph(sub_nodes).number_of_edges() + (HT + 1) > HT*k:
                return False
    return True


###############################################################
# Generate random graphs
random.seed(701215003254586823)  # For reproducibility
# seed = random.randrange(sys.maxsize)
# rng = random.Random(seed)
# print("Seed was:", seed)

graphs = []
HT = 3

for _ in range(20):
    num_nodes = random.randint(4, 8)
    num_edges = (HT*num_nodes- (HT+1))/(HT-1)
    G = nx.gnm_random_graph(num_nodes, num_edges)
    graphs.append(G)

# Visualize and label the graphs
fig, axes = plt.subplots(4, 5, figsize=(20, 15))
for i, G in enumerate(graphs):
    ax = axes[i//5, i%5]
    is_laman = is_laman_graph(G, HT)
    label = str(HT) + "-Laman" if is_laman else "Not {}-Laman".format(HT)
    nx.draw(G, ax=ax, with_labels=True, node_size=700, 
            node_color='skyblue' if is_laman else 'lightgray')
    ax.set_title(label)
# plt.tight_layout()
plt.show()


#fig.savefig("2_Laman_examples.pdf")

#####################################################################
# Define the Henneberg Type (HT) for the condition
HT = 3  # Change this value according to the specific HT-Laman condition you are checking for

# Initialize a list to store graphs that satisfy the HT-Laman condition
laman_graphs = []

# Iterate over all graphs in the Graph Atlas with up to seven nodes
for n in range(1, 8):  # Graphs with up to seven nodes
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() == n and is_laman_graph(G, HT):
            laman_graphs.append(G)

# Now laman_graphs contains all graphs up to seven nodes that satisfy the HT-Laman condition
print(f"Found {len(laman_graphs)} graphs that satisfy the HT-Laman condition.")

# Create a figure with subplots
nrows = 2
ncols = 5
fig, axes = plt.subplots(nrows, ncols, figsize=(6*ncols, 6*nrows))
fig.suptitle(f'List of {HT}-Laman graphs up to seven nodes', fontsize=20)
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Flatten the axes array for easy iteration
axes_flat = axes.flatten()

for i, G in enumerate(laman_graphs):
    if i >= nrows*ncols:  # In case we have more than 20 graphs, break out of the loop
        break
    ax = axes_flat[i]
    nx.draw(G, ax=ax, with_labels=True, node_size=700, font_weight='bold', node_color='skyblue')
    ax.set_title(f'V = {G.number_of_nodes()}, E = {G.number_of_edges()}')

# If there are any remaining subplots, disable them
for j in range(i + 1, len(axes_flat)):
    axes_flat[j].axis('off')

plt.show()

fig.savefig(f'{HT}_Laman_up_to_7_nodes.pdf')