import random, copy, sympy
import prairielearn as pl
from sympy import symbols, FiniteSet, Union, Intersection, ProductSet, sympify
from sympy.functions.combinatorial.numbers import nC, nP

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.choices(range(10),k=random.randint(3,6))
    b = random.choices(range(10),k=random.randint(3,6))
    A = FiniteSet(*a)
    B = FiniteSet(*b)
    
    # Put these two integers into data['params']
    data['params']['a'] = sympy.latex(A)
    data['params']['b'] = sympy.latex(B)
    
    op = random.choice(['\\cup', '\\times'])
    pow_a = random.choice([True, False])
    pow_b = random.choice([True, False])
    
    a_str = "A "
    b_str = " B"
    
    op_str = a_str + op + b_str
        
    data['params']['operation'] = op_str
    
    if op == '\\cup':
        C = Union(A,B)
        ind = random.randint(0,2)
    elif op == '\\times':
        C = ProductSet(A,B)
        ind = random.randint(0,1)

    n = len(C)
    r = random.randint(2,min(9,n-1))
    
    if ind == 0:
        scen = ["ways to choose ", "ways to select "]
        data['params']['instruction'] = random.choice(scen) + " " + str(r) + " elements from $C$ "
        data['correct_answers']['c'] = nC(n,r)
    elif ind == 1:
        scen = ["ways to arrange ", "ways to order "]
        data['params']['instruction'] = random.choice(scen) + " " + str(r) + " elements from $C$ "
        data['correct_answers']['c'] = nP(n,r)
    elif ind == 2:
        r = random.randint(4,9)
        data['params']['instruction'] = "strings of length " + str(r) + " made up of characters from $C$ "
        data['correct_answers']['c'] = sympify(n ** r)