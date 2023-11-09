import random, copy, math
from sympy.stats import P,Die,Coin,Binomial,variance,E
from sympy import Eq,Rational,latex
import prairielearn as pl

def generate(data):

    prob = Rational(random.randint(1,9),10)
    flips = random.randint(2,10)*10
    heads = random.randint(10,flips-1)
    
    X = Binomial('X',flips,prob)
    e = E(X)
    k = random.randint(1,min(e,flips-e)-1)
    var = variance(X)
    cheb = var/(k**2)
    
    rng, ans = random.choice([("outside",cheb), ("between", 1 - cheb)])
    
    
    
    # Put these two integers into data['params']
    data['params']['prob'] = latex(prob)
    data['params']['flips'] = flips
    data['params']['low'] = int(e-k)
    data['params']['high'] = int(e+k)
    data['params']['rng'] = rng
    

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(ans)
