# Laman Graphs and Graph Neural Networks

## Introduction

As a cornerstone in graph theory, the Laman graphs are a family of sparse graphs that minimally rigid, named after a Dutch mathematician Gerard Laman. Formally a graph is call *Laman* if it satisfies the following two conditions
- global condition: it has exactly $V$ vertices and $2 V-3$ edges.
- local condition: for any subgraph with $k$ vertices, there are at most $2 k-3$ edges.

Intuitively, think of a graph as a bunch of rods joint together. *Laman* graphs are the ones that are rigid and **cannot** be deformed preserving the length of all rods.

For example, the following graphs are Laman

<img width="560" alt="image" src="https://github.com/jingxiangwu/laman/assets/110117607/ebfb38e4-1b34-4a96-8cc9-f2301167cc20">

while these are not Laman

<img width="726" alt="image" src="https://github.com/jingxiangwu/laman/assets/110117607/49e2e83f-aadc-4f19-9f5b-e8890964304a">

The number of Laman graphs is cataloged in [OEIS](https://oeis.org/A227117).


They are pivotal in structural engineering for designing frameworks that are stable yet use minimal material, ensuring both stability and efficiency. In robotics, Laman graphs provides flexible and yet stable structures, making the robot more robust and adaptable. They also have important applications in computational biology, providing insights into molecular stability and interactions. 

## Generalization to n-Laman Graphs

It turns out Laman graphs appear as fundament objects in the study of quantum field theories as well where the notion can be naturally generalized, dubbed as **n-Laman graphs**.  A graph is called n-Laman if
- global condition: let $V$ be the number of vertices and $E$ be the number of edges
$$n V=(n-1)E+n+1$$
- local condition: for any subgraph, let $v$ be the number of vertices and $e$ be the number of edges
$$n v \geq(n-1)e+n+1$$

Roughly speaking, perturbative calculations in quantum field theories are organized in (Feyman) graphs. A priori, any graph needs to be considered. However, it turns out twisted quantum field theories has an intricate hidden structure that the only graphs with nontrivial contributions are n-Laman graphs. See my paper ([Feynman Diagrams in Four-Dimensional
Holomorphic Theories and the Operatope](https://arxiv.org/abs/2207.14321)) for more details. See also the following articles for discussions along these lines
- Unraveling the Holomorphic Twist: Central Charges. [arXiv: 2311.04304](https://arxiv.org/abs/2311.04304)
- On $\frac18$-BPS black holes and the chiral algebra of $\mathcal{N}=4$ SYM. [arXiv: 2310.20086](https://arxiv.org/abs/2310.20086)
- Semi-Chiral Operators in 4d ${N}=1$ Gauge Theories. [arXiv: 2306.01039](https://arxiv.org/abs/2306.01039)


## Outline

- **Mathematica Code**: Implements generation, validation, and cataloging of generalized n-Laman graphs.
- **Python Code**: Uses NetworkX for generating random graphs and verifying n-Laman conditions.
- **Dataset**: encoded in [torch_geometric.data objects](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.data.Data.html#torch_geometric.data.Data), where `feature` is the degree of each nodes and truth label is the Laman-ness. See [database](./laman_graphs_1e4dataset12nodesHT2.pt)
- **ML to identify Laman graphs**: employing PyTorch Geometric/Graph Neural Network (GNN) to do the fast identification. This is a priori quite challenging for graph neural network. The main reason is because Laman-ness concerns about the density of the edges for **all** subgraphs of arbitrary size instead of local information of each nodes. Nevertheless, I seem to find two promising architectures so far are Graph Convolutional Network and Hierarchical Graph Neural Network.
- .....

<!---
<img width="863" alt="image" src="https://github.com/jingxiangwu/laman/assets/110117607/962de71f-f771-4c87-8c26-3d3da363fd91">
-->

## Training and Evaluations
Here is the size of our datasets

| V              | 2   | 3   | 4   | 5   | 6     | 7     | 8      | 9      | 10        | 11      | 12              |
|----------------|-----|-----|-----|-----|-------|-------|--------|--------|-----------|---------|-----------------|
| $N_{n=2}$      | 1   | 1   | 1   | 3   | 13    | 70    | 608    | 7222   | 110132    | 2039273 | 44176717         |
| $N_{n=3}$      | 1   | 0   | 1   | 0   | 2     | 0     | $\geq 14/476$ | 0 | $\geq 199/22408$ | 0       | $\geq 2290/487596$ |


|                 | Accuracy  | Precision | Recall    | F1-score  | AUC-ROC   |
|-----------------|-----------|-----------|-----------|-----------|-----------|
| n=2, V=9        | 0.994249  | 0.986395  | 0.998279  | 0.992301  | 0.999949  |
| n=3, V=12       | 0.999303  | 0.883858  | 0.980349  | 0.929607  | 0.999867  |





## Tips
As I recently switched to a MacBook with Apple Silicon chip, it becomes quite non straightforward to install PyTorch Geometric. I have included a detailed guide on the installation on M1 Macs, please see [Installation Guide](./install_geometric.md).



## Related Projects

In addition to the work presented in this repository, I am also collaborating on an ongoing project focused on the study of Laman graphs in twisted quantum field theories. For more information, please visit [TwistedQFTs on GitHub](https://github.com/TwistedQFTs).
