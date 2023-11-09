import random, copy
from sympy import sieve

def generate(data):
    
    primes = [i for i in sieve.primerange(7,19)]

    p = random.choice(primes)
    a = random.randrange(2, p)

    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['p'] = p

    # Compute the sum of these two integers
    b = pow(a, -1, p)

    # Put the sum into data['correct_answers']
    data['correct_answers']['b'] = b
