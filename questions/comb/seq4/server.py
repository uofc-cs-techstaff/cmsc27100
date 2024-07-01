import prairielearn as pl
import random, copy
from sympy.functions.combinatorial.numbers import nC, nP
from sympy import sympify

def generate(data):

    l = random.randint(3, 8)
    pieces1 = ["♟","♟","♟","♟","♟","♟","♟","♟"]
    pieces3 = ["♙","♙","♙","♙","♙","♙","♙","♙"]
    pieces2 = ["♜","♞","♝","♛","♚","♖","♘","♗","♕","♔"]
    
    pieces = random.choice([pieces1,pieces2,pieces2,pieces3])
    a = sorted(random.sample(pieces,k=l))
    str_a = ''.join(a)
    
    data['params']['pieces'] = str_a
    
    data['correct_answers']['c'] = pl.to_json(nC(64,l)) if pieces == pieces1 or pieces == pieces3 else pl.to_json(nP(64,l))
    