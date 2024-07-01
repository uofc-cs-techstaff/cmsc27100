import prairielearn as pl
import random, copy
from sympy import sympify

def generate(data):

    l = random.randint(6, 16)
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    version = "grey" #random.choice(["grey","goldenrod"])
    colours = ["darkseagreen","grey","grey"]

    word = random.sample(alphabet, k=5)
    sol = [(x,random.choice(colours)) for x in word]
    # Put these two integers into data['params']
    for i in range(5):
        data['params']['a'+str(i+1)] = sol[i][0]
        data['params']['col'+str(i+1)] = sol[i][1]

    cols = [x[1] for x in sol]
    #rem = 5 - cols.count("darkseagreen")
    
    if version == "grey":
        rem = cols.count("grey")
        alphs = 26 - rem
        data['correct_answers']['c'] = pl.to_json(sympify(alphs ** rem))
    else:
        data['correct_answers']['c'] = pl.to_json(sympify(0))
    
    

