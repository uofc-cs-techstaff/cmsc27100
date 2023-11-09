import random, copy, sympy
from sympy import symbols, FiniteSet, Union, Intersection, ProductSet, Complement

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.choices(range(10),k=random.randint(2,5))
    b = random.choices(range(10),k=random.randint(3,5))
    A = FiniteSet(*a)
    B = FiniteSet(*b)
    
    # Put these two integers into data['params']
    data['params']['a'] = sympy.latex(A)
    data['params']['b'] = sympy.latex(B)
    
    op = random.choice(['\\cup', '\\cap', '\\times', '\\setminus'])
    pow_a = random.choice([True, False])
    pow_b = random.choice([True, False])
    if pow_a or pow_b:
        pow_ab = False
    else:
        pow_ab = random.choice([True, False])
    
    if pow_a:
        A = A.powerset()
        a_str = "\mathcal P(A) "
    else:
        a_str = "A "
    
    if pow_b:
        B = B.powerset()
        b_str = " \mathcal P(B)"
    else:
        b_str = " B"
    
    if pow_ab:
        op_str = "\mathcal P(" + a_str + op + b_str + ")"
    else:
        op_str = a_str + op + b_str
        
    data['params']['operation'] = op_str
    
    if op == '\\cup':
        C = Union(A,B)
    elif op == '\\cap':
        C = A.intersect(B)
    elif op == '\\times':
        C = ProductSet(A,B)
    elif op == '\\setminus':
        C = Complement(A,B)
    
    if pow_ab:
        C = C.powerset()
    
    data['correct_answers']['c'] = len(C)