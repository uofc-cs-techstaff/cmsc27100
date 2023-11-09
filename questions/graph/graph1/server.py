import random, copy, math
import prairielearn as pl
import numpy as np
import networkx as nx
from networkx.generators.random_graphs import fast_gnp_random_graph
from networkx.drawing.nx_agraph import write_dot

def generate(data):
    n = random.randint(5,7)
    mat = np.random.randint(2,size=(n,n))
    data['params']['labels'] = pl.to_json([str(x+1) for x in range(n)])
    data['params']['matrix'] = pl.to_json(mat)
    
    for i in range(4):
        G = fast_gnp_random_graph(n,0.4)
        write_dot(G,"g.dot")
        f = open("g.dot","r")
        gr = f.read()
        f.close()
        data['params']['g'+str(i)] = gr
        
    G = fast_gnp_random_graph(n,0.6)
    write_dot(G,"g.dot")
    f = open("g.dot","r")
    gr = f.read()
    f.close()
    data['params']['g4'] = gr
    
    node_mapping = dict(zip(G.nodes(), sorted(G.nodes(), key=lambda k: random.random())))
    G_new = nx.relabel_nodes(G, node_mapping)
    write_dot(G_new,"g.dot")
    f = open("g.dot","r")
    gr = f.read()
    f.close()
    data['params']['g5'] = gr


    data['correct_answers']['d'] = n

