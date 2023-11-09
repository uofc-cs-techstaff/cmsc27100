import numpy
import sympy

def generate(data):

    # Create a variable
    p,q,r = sympy.symbols('p q r')

    # Randomize the number of variables
    num_terms = numpy.random.random_integers(3,6)

    # Randomize the coefficients (make sure the leading coefficient is non-zero)
    minterms = numpy.random.choice(range(0,8),num_terms,False).tolist()

    # Create the boolean formula
    f = sympy.logic.POSform([p,q,r],minterms)
    #sat = numpy.random.choice(list(sympy.logic.inference.satisfiable(f,all_models=True)))
    
    data["params"]["ptqtrt"] = str(f.subs({p: True, q: True, r: True}))
    data["params"]["ptqtrf"] = str(f.subs({p: True, q: True, r: False}))
    data["params"]["ptqfrt"] = str(f.subs({p: True, q: False, r: True}))
    data["params"]["ptqfrf"] = str(f.subs({p: True, q: False, r: False}))
    data["params"]["pfqtrt"] = str(f.subs({p: False, q: True, r: True}))
    data["params"]["pfqtrf"] = str(f.subs({p: False, q: True, r: False}))
    data["params"]["pfqfrt"] = str(f.subs({p: False, q: False, r: True}))
    data["params"]["pfqfrf"] = str(f.subs({p: False, q: False, r: False}))
    
    data["params"]["dp"] = sympy.latex(p)
    data["params"]["dq"] = sympy.latex(q)
    data["params"]["dr"] = sympy.latex(r)
    data["params"]["f"] = sympy.latex(f)

if __name__ == "__main__":
    generate({"params":{}})
