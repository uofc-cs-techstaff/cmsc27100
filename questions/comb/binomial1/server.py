import random, copy
import prairielearn as pl
from sympy import sieve, poly, Poly, ground_roots, latex, Symbol, Rational

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(1,5)
    b = random.choice([i for i in range(-4,4) if i != 0])
    k = random.randint(4,8)
    
    (s,t) = random.choice([("a","b"),("b","c"),("c","d"),("f","g"),("g","h"), ("k","l"), ("m","n"), ("p","q"), ("r","s"), ("s","t"), ("u","v"),("x","y"), ("y","z")])
    
    x = Symbol(s)
    y = Symbol(t)
    
    binom = a*x + b*y
    
    if random.choice([True,False]):
        binom = binom.subs(y,1)
        
    p = poly(binom**k)
    
    data['params']['eqn'] = latex(p.as_expr())
    data['params']['variables'] = s + ", " + t

    data['correct_answers']['z'] = pl.to_json(binom)
