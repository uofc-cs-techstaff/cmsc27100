import random, copy, math
from sympy.stats import P,Die,Coin
from sympy import Eq
import prairielearn as pl

def generate(data):

    size = random.choice([4,6,8,10,12,20])
    sum = random.randint(2,size*2)
    step = random.randint(2,10)
    
    X,Y = Die('X',size), Die('Y',size)
    
    p = P(Eq(X+Y,sum))
    
    ans = 1/p
    
    # Put these two integers into data['params']
    data['params']['size'] = size
    data['params']['step'] = step
    data['params']['sum'] = sum
    

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(ans)
