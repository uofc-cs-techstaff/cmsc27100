import random, copy
from sympy.functions.combinatorial.numbers import nC 

def generate(data):

    l = random.randint(4, 6)
    pieces = ["🀀", "🀁", "🀂", "🀃", "🀄", "🀅", "🀆", "🀇", "🀈", "🀉", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏", "🀐", "🀑", "🀒", "🀓", "🀔", "🀕", "🀖", "🀗", "🀘", "🀙", "🀚", "🀛", "🀜", "🀝", "🀞", "🀟", "🀠", "🀡"]

    #testing testing
    #hopefullt this is enough to shwo that it isn't binary

    a = sorted(random.sample(pieces,k=l))
    str_a = ''.join(a)
    
    data['params']['pieces'] = str_a
    
    base = 64
    res = 0
    for c in set(a):
        num = str_a.count(c)
        
    
    # Compute the sum of these two integers
    c = 1

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
