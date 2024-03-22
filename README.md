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
$$n e \geq(n-1)e+n+1$$

Roughly speaking, perturbative calculations in quantum field theories are organized in (Feyman) graphs. A priori, any graph needs to be considered. However, it turns out twisted quantum field theories has an intricate hidden structure that the only graphs with nontrivial contributions are n-Laman graphs. See my paper ([Feynman Diagrams in Four-Dimensional
Holomorphic Theories and the Operatope](https://arxiv.org/abs/2207.14321)) for more details. See also the following articles for discussions along these lines
- Unraveling the Holomorphic Twist: Central Charges. [arXiv: 2311.04304](https://arxiv.org/abs/2311.04304)
- On $\frac18$-BPS black holes and the chiral algebra of $\mathcal{N}=4$ SYM. [arXiv: 2310.20086](https://arxiv.org/abs/2310.20086)
- Semi-Chiral Operators in 4d ${N}=1$ Gauge Theories. [arXiv: 2306.01039](https://arxiv.org/abs/2306.01039)


## Contents

- **Mathematica Code**: Implements generation, validation, and cataloging of generalized n-Laman graphs.
- **Python Code**: Uses NetworkX for generating random graphs and verifying n-Laman conditions.
- **Machine Learning Project**: A on-going project employing PyTorch Geometric to identify and generate generalized n-Laman graphs through Reinforcement Learning.
- .....

## Acknowledgments

Thanks to all collaborators for their invaluable insights and support in this ongoing exploration of Laman graphs and their generalizations. Contributions are welcome.

## Related Projects

In addition to the work presented in this repository, I am also collaborating on an ongoing project focused on the study of Laman graphs in twisted quantum field theories. For more information, please visit [TwistedQFTs on GitHub](https://github.com/TwistedQFTs).
