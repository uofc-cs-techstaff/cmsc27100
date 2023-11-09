import random, copy, sympy
from sympy import symbols, FiniteSet, Union, Intersection, ProductSet, Complement

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.choices(range(10),k=random.randint(2,9))
    b = random.choices(range(10),k=random.randint(2,4))
    A = FiniteSet(*a)
    B = random.choice([FiniteSet(*b),FiniteSet(*b).powerset()])
    
    # Put these two integers into data['params']
    data['params']['a'] = sympy.latex(A)
    data['params']['b'] = sympy.latex(B)

    if len(A) > len(B):
        prop = [["injective/one-to-one", "false"],["surjective/onto", "true"],["bijective/correspondence", "false"]]
    elif len(A) < len(B):
        prop = [["injective/one-to-one", "true"],["surjective/onto", "false"],["bijective/correspondence", "false"]]
    else:
        prop = [["injective/one-to-one", "true"],["surjective/onto", "true"],["bijective/correspondence", "true"]]
        
    random.shuffle(prop)
        
    for i in range(3):
        data['params']['text'+str(i)] = prop[i][0]
        data['params']['ans'+str(i)] = prop[i][1]
