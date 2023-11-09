import random, copy
from sympy import sieve, Poly, ground_roots, latex
from sympy.ntheory.modular import solve_congruence
from sympy.abc import x

def generate(data):
    primes = [(3,5,5),(3,7,7),(3,11,11),(3,13,13),(5,13,12),(7,13,13)]

    # Sample two random integers between 5 and 10 (inclusive)
    (p,q,b) = random.choice(primes)
    m = p*q
    a = random.choices([y for y in list(range(1-q,-1)) + list(range(2,q)) if y%p != 0 and y%q != 0],k=3)

    # Put these two integers into data['params']


    eqn = (x**b) + a[1]*x + a[2]
    
    data['params']['m'] = m
    data['params']['eqn'] = latex(eqn)

    s1 = ground_roots(Poly(eqn, modulus=p))
    s2 = ground_roots(Poly(eqn, modulus=q))

    if s1 == {} or s2 == {}:
        return generate(data)
    else:
        a1 = int(list(s1)[0])%p
        a2 = int(list(s2)[0])%q
        y = solve_congruence((a1,p),(a2,q))
        data['correct_answers']['c'] = y[0]
