from main.dimacs import load_weighted_graph
from main.lab4.graph import Graph

path = 'graphs/chordal/example-fig5'

g = Graph(load_weighted_graph(path))
print(g.check_peo())

