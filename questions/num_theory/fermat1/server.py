import random, copy
from sympy import sieve

def generate(data):
    primes = list(sieve.primerange(3,15))

    # Sample two random integers between 5 and 10 (inclusive)
    m = random.choice(primes)
    a = random.choice(list(range(-m+1,-1)) + list(range(2,m)))
    b = random.randint(200,5000)
    


    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['m'] = m

    # Compute the sum of these two integers
    c = pow(a,b,m)

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
