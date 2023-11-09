import random, copy, math
import prairielearn as pl
import numpy as np
import networkx as nx
from networkx.generators.random_graphs import fast_gnp_random_graph, connected_watts_strogatz_graph
from networkx.drawing.nx_agraph import write_dot
from networkx.algorithms.connectivity import minimum_edge_cut

def generate(data):
    n = random.randint(20,200)
    k = random.randint(3,min(n,50))

    data['params']['v'] = n
    data['params']['k'] = k
    
    ans = n-k
    
    data['correct_answers']['n'] = ans

