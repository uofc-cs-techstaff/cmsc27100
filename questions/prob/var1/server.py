import random, copy, math
from sympy.stats import P,Die,Coin,Binomial,variance,E
from sympy import Eq,Rational,latex
import prairielearn as pl

def generate(data):

    prob = Rational(random.randint(1,9),10)
    flips = random.randint(2,10)*10
    heads = random.randint(10,flips-1)
    
    X = Binomial('X',flips,prob)
    exp = E(X)
    var = variance(X)
    
    #ans = p * (1-p)**(step-1)
    
    # Put these two integers into data['params']
    data['params']['prob'] = latex(prob)
    data['params']['flips'] = flips
    #data['params']['sum'] = sum
    

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(var)
