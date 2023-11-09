import random, copy
from sympy import sieve


def generate(data):

    primes = list(sieve.primerange(7,19))

    m = random.choice(primes)
    a = random.choice([x for x in list(range(-50,-m)) + list(range(m,100)) if x%m != 0])
    b = random.choice([x for x in list(range(1,m))])


    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['m'] = m

    # Compute the sum of these two integers
    c = (pow(a, -1, m) * b) % m

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
