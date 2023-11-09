import random, copy, math
import prairielearn as pl
import numpy as np
import networkx as nx
from networkx.generators.random_graphs import fast_gnp_random_graph, connected_watts_strogatz_graph, random_regular_graph
from networkx.drawing.nx_agraph import write_dot
from networkx.algorithms.shortest_paths.generic import shortest_path_length

def generate(data):
    n = random.randint(8,16)

    #G = fast_gnp_random_graph(n,0.5)
    deg = random.randint(2,n-2)
    while n*deg % 2 == 1:
        deg = random.randint(2,n-2)
    regular = random.choice([True,False])
    
    G = random_regular_graph(deg,n)
    if not regular:
        G = fast_gnp_random_graph(n,0.5)
    
    node_mapping = dict(zip(G.nodes(), sorted(G.nodes(), key=lambda k: random.random())))
    G = nx.relabel_nodes(G, node_mapping)
    write_dot(G,"g.dot")
    f = open("g.dot","r")
    gr = f.read()
    f.close()
    data['params']['g0'] = gr
    
    data['correct_answers']['n'] = deg
    if not regular:
        data['correct_answers']['n'] = 999

