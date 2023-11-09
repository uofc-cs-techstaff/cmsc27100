import random, copy, math
from sympy.stats import P,Die,Coin,density
from sympy import Eq
import prairielearn as pl

def generate(data):

    dice = random.choices([4,6,8,10,12,20],k=3)
    sum = random.choice([5,6,dice[0]+dice[1]+dice[2]-random.randint(2,4)])
    
    X = Die('X',random.randint(6,20))
    a = random.sample([i for i in range(1,len(density(X).dict))],k=2)
    
    p_a = P(Eq(X % a[0], 0))
    p_b = P(Eq(X % a[1], 0))
    p_c = P(Eq(X % a[1], 0) & Eq(X % a[0], 0))
    
    
    # Put these two integers into data['params']
    data['params']['a'] = a[0]
    data['params']['b'] = a[1]
    data['params']['d0'] = len(density(X).dict)


    
    data['params']['pos'] = "false"
    data['params']['neg'] = "false"
    data['params']['ind'] = "false"
    
    if p_a * p_b < p_c:
        data['params']['pos'] = "true"
    elif p_a * p_b > p_c:
        data['params']['neg'] = "true"
    else:
        data['params']['ind'] = "true"

