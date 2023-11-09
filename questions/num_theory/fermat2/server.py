import random, copy
from sympy import sieve, Poly, ground_roots, latex
from sympy.abc import x

def generate(data):
    primes = list(sieve.primerange(5,15))

    # Sample two random integers between 5 and 10 (inclusive)
    m = random.choice(primes)
    a = random.choices(list(range(1-m,-1)) + list(range(2,m)),k=3)
    b = random.choice([m-1,m,m+m-1])

    # Put these two integers into data['params']


    eqn = a[0]*(x**b) + a[1]*x + a[2]
    
    data['params']['m'] = m
    data['params']['eqn'] = latex(eqn)

    sol = ground_roots(Poly(eqn, modulus=m))
    if sol == {}:
        return generate(data)
    else:
        data['correct_answers']['c'] = int(list(sol)[0])%m
