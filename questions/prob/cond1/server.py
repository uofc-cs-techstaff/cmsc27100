import random, copy, math
from sympy.stats import P,Die,Coin,density
from sympy import Eq,latex
import prairielearn as pl

def generate(data):

    dice = random.choices([4,6,8,10,12,20],k=3)
    sum = random.randint(5, dice[0]+dice[1]+dice[2]-2) #random.choice([5,6,dice[0]+dice[1]+dice[2]-random.randint(2,4)])
    
    X,Y,Z = Die('X'),Die('Y'),Die('Z') #Die('X',dice[0]), Die('Y',dice[1]), Die('Z',dice[2])
    sum = random.randint(5,16)
    
    ans,op = random.choice([(X+Y+Z > sum, "greater than"),(X+Y+Z < sum, "less than"), (Eq(X+Y+Z,sum), "equal to")])
    die = random.choice([X,Y,Z])
    e = random.randint(2,len(density(die).dict)-1)
    cond = random.choice([Eq(die,e), die > e, die < e])
    
    
    # Put these two integers into data['params']
    data['params']['d0'] = dice[0]
    data['params']['d1'] = dice[1]
    data['params']['d2'] = dice[2]
    data['params']['res'] = sum
    data['params']['op'] = op
    data['params']['cond'] = latex(cond)

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = pl.to_json(P(ans,cond))
