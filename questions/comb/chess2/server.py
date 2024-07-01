import random, copy
import prairielearn as pl
from sympy.functions.combinatorial.numbers import nC 
from sympy import sympify

def generate(data):

    l = random.randint(5, 7)
    pieces = ["♜","♜","♞","♞","♝","♝","♛","♚","♟","♟","♟","♟","♟","♟","♟","♟","♙","♙","♙","♙","♙","♙","♙","♙","♖","♖","♘","♘","♗","♗","♕","♔"]
    a = sorted(random.sample(pieces,k=l))
    str_a = ''.join(a)
    
    data['params']['pieces'] = str_a
    
    base = 64
    res = 1
    for c in set(a):
        num = str_a.count(c)
        res = res * int(nC(base, num))
        base = base - num
        

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = pl.to_json(sympify(res))
