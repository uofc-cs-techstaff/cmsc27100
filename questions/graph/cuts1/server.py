import random, copy, math
import prairielearn as pl
import numpy as np
import networkx as nx
from networkx.generators.random_graphs import fast_gnp_random_graph, connected_watts_strogatz_graph
from networkx.drawing.nx_agraph import write_dot
from networkx.algorithms.connectivity import minimum_edge_cut

def generate(data):
    n = random.randint(8,11)

    G = fast_gnp_random_graph(n,0.5)
    #G = connected_watts_strogatz_graph(n,random.choice([3,5]),0.5)
    node_mapping = dict(zip(G.nodes(), sorted(G.nodes(), key=lambda k: random.random())))
    G = nx.relabel_nodes(G, node_mapping)
    write_dot(G,"g.dot")
    f = open("g.dot","r")
    gr = f.read()
    f.close()
    data['params']['g0'] = gr
    
    data['correct_answers']['n'] = len(minimum_edge_cut(G))

