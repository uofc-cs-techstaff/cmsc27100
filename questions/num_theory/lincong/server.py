import random, copy
from sympy import sieve, Poly, solve_poly_system
from sympy.abc import x,y
from sympy.solvers import solve

def generate(data):

    primes = list(sieve.primerange(7,18))

    m = random.choice(primes)
    a = random.choices(list(range(2,m)),k=6)
    
    # Put these two integers into data['params']
    for i in range(len(a)):
        data['params']['a'+str(i)] = a[i]
    data['params']['m'] = m
    
    eq1 = Poly(a[0]*x + a[1]*y - a[2], modulus=m)
    eq2 = Poly(a[3]*x + a[4]*y - a[5], modulus=m)
    
    try:
        ans = solve_poly_system([eq1,eq2],[x,y])
        if ans is None:
            return generate(data)
        else:
            # Put the sum into data['correct_answers']
            data['correct_answers']['x'] = int(ans[0][0]%m)
            data['correct_answers']['y'] = int(ans[0][1]%m)
    except:
        return generate(data)
