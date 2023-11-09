import random, copy
from sympy import sieve
from sympy.ntheory.modular import solve_congruence

def generate(data):

    primes = list(sieve.primerange(3,15))

    ms = random.sample(primes,3)
    bs = [random.choice(list(range(1,m))) for m in ms]
    
    # Put these two integers into data['params']
    for i in range(len(ms)):
        data['params']['m'+str(i)] = ms[i]
        data['params']['a'+str(i)] = bs[i]
    
    x = solve_congruence(*zip(bs,ms))
    
    data['correct_answers']['x'] = x[0]
