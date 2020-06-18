# Network-Flows-Stuff

Constant work in progress here. So far, this repo contains:

* **network_flows.py**, containing helper functions to create data structures for network flow problems for now (really for converting a network represented as an edge list to its equivalent adjacency matrix and vice versa)
* **Minimum_Spanning_Tree_Exploration.ipynb**, a notebook exploring the [Minimum Spanning Tree Problem](https://en.wikipedia.org/wiki/Minimum_spanning_tree), mainly some kind of hacky implementations of [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) and [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) to solve the problem in a couple small example networks

### In the Future...

Do the same thing with Minimum Spanning Tree Problem for:

* Shortest Path Problem
* Min-Cost Flow Problem
* Maximum Flow Problem

Build out **network_flows.py** to incorporate different network properties/metrics and data structures. For the latter, this might include converting adjacency matrix and edge list network representaitons into:

* `NetworkX` graph objects
* Inputs for optimization tools such as `scipy.optimize`, `or-tools` or `cvxopt`