import random, copy
from sympy.functions.combinatorial.numbers import nC, nP

def generate(data):

    l = random.randint(3, 8)
    pieces1 = ["♟","♟","♟","♟","♟","♟","♟","♟"]
    pieces3 = ["♙","♙","♙","♙","♙","♙","♙","♙"]
    pieces2 = ["♜","♞","♝","♛","♚","♖","♘","♗","♕","♔"]
    
    pieces = random.choice([pieces1,pieces2,pieces2,pieces3])
    a = sorted(random.sample(pieces,k=l))
    str_a = ''.join(a)
    
    data['params']['pieces'] = str_a
    
    if pieces == pieces1 or pieces == pieces3:
        data['correct_answers']['c'] = int(nC(64,l))
    else:
        data['correct_answers']['c'] = int(nP(64,l))
