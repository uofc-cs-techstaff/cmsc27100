import random, copy, math
from sympy.stats import P,Die,Coin,density
from sympy import Eq,latex,Rational
import prairielearn as pl

def generate(data):

    length = random.randint(8,16)
    err = Rational(1,random.randint(3,6))
    denom = random.choice([3,4,5,6,8,10])
    send0 = Rational(random.randint(1,denom-1),denom)
    send1 = 1-send0
    
    r0s0 = 1-err
    r1s1 = 1-err
    r0s1 = err
    r1s0 = err
    
    r0 = r0s0 * send0 + r0s1 * send1
    r1 = r1s1 * send1 + r1s0 * send0
    
    s0r0 = (r0s0 * send0)/r0
    s1r1 = (r1s1 * send1)/r1
    s0r1 = (r1s0 * send0)/r1
    s1r0 = (r0s1 * send1)/r0
    
    send, rec, ans = random.choice([(0,0,s0r0),(0,1,s0r1),(1,0,s1r0),(1,1,s1r1)])
    
    # Put these two integers into data['params']
    data['params']['len'] = int(length)
    data['params']['err'] = latex(err)
    data['params']['s0'] = latex(send0)
    data['params']['s1'] = latex(send1)
    data['params']['send'] = send
    data['params']['rec'] = rec

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(ans)
