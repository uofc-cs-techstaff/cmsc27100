import random
import prairielearn as pl
from sympy import sympify

def generate(data):
    n = random.randint(20,200)
    k = random.randint(3,min(n,50))

    data['params']['v'] = n
    data['params']['k'] = k
    
    ans = n-k
    
    data['correct_answers']['n'] = pl.to_json(sympify(ans))

