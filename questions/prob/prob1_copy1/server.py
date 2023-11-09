import random, copy, math
from sympy.stats import P,Die,Coin
from sympy import Eq
import prairielearn as pl

def generate(data):

    dice = random.choices([4,6,8,10,12,20],k=3)
    sum = random.choice([5,6,dice[0]+dice[1]+dice[2]-random.randint(2,4)])
    
    X,Y,Z = Die('X',dice[0]), Die('Y',dice[1]), Die('Z',dice[2])
    
    ans,op = random.choice([(P(X+Y+Z > sum), "greater than"),(P(X+Y+Z < sum), "less than"), (P(Eq(X+Y+Z,sum)), "equal to")])
    
    
    # Put these two integers into data['params']
    data['params']['d0'] = dice[0]
    data['params']['d1'] = dice[1]
    data['params']['d2'] = dice[2]
    data['params']['res'] = sum
    data['params']['op'] = op

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(ans)
