# Laman Graphs and Graph Neural Networks

## Introduction

As a cornerstone in graph theory, the Laman graphs are a family of sparse graphs that minimally rigid, named after a Dutch mathematician Gerard Laman. Formally a graph is call *Laman* if it satisfies the following two conditions
- global condition: it has exactly $V$ vertices and $2 V-3$ edges.
- local condition: for any subgraph with $k$ vertices, there are at most $2 k-3$ edges.

They are pivotal in structural engineering for designing frameworks that are stable yet use minimal material, ensuring both stability and efficiency. In robotics, Laman graphs provides flexible and yet stable structures, making the robot more robust and adaptable. They also have important applications in computational biology, providing insights into molecular stability and interactions. 

## Generalization to n-Laman Graphs

It turns out Laman graphs appear as fundament objects in the study of quantum field theories as well where the notion can be naturally generalized, dubbed as **n-Laman graphs**. See my paper ([Feynman Diagrams in Four-Dimensional
Holomorphic Theories and the Operatope](https://arxiv.org/abs/2207.14321)) for more details. A graph is called n-Laman if
- global condition: let $V$ be the number of vertices and $E$ be the number of edges
$$n V=(n-1)E+n+1$$
- local condition: for any subgraph, let $v$ be the number of vertices and $e$ be the number of edges
$$n e \geq(n-1)e+n+1$$



## Repository Contents

- **Mathematica Code**: Implements generation, validation, and cataloging of generalized n-Laman graphs.
- **Python Code**: Uses NetworkX for generating random graphs and verifying n-Laman conditions.
- **Machine Learning Project**: A on-going project employing PyTorch Geometric to identify and generate generalized n-Laman graphs through Graph Neural Networks (GNNs).
- .....

## Acknowledgments

Thanks to all collaborators for their invaluable insights and support in this ongoing exploration of Laman graphs and their generalizations. Contributions are welcome.
