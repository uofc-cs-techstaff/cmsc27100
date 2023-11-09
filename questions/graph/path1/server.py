import random, copy, math
import prairielearn as pl
import numpy as np
import networkx as nx
from networkx.generators.random_graphs import fast_gnp_random_graph, connected_watts_strogatz_graph
from networkx.drawing.nx_agraph import write_dot
from networkx.algorithms.shortest_paths.generic import shortest_path_length

def generate(data):
    n = random.randint(8,16)

    #G = fast_gnp_random_graph(n,0.5)
    G = connected_watts_strogatz_graph(n,random.choice([3,5]),0.5)
    node_mapping = dict(zip(G.nodes(), sorted(G.nodes(), key=lambda k: random.random())))
    G = nx.relabel_nodes(G, node_mapping)
    write_dot(G,"g.dot")
    f = open("g.dot","r")
    gr = f.read()
    f.close()
    data['params']['g0'] = gr
    
    vs = random.sample(list(range(n)),k=2)
    data['params']['s'] = vs[0]
    data['params']['t'] = vs[1]
    
    
    data['correct_answers']['n'] = shortest_path_length(G,vs[0],vs[1])

