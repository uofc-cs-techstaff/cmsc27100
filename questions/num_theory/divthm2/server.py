import random, copy, math

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    q = random.randint(2, 20)
    r = random.randint(1, 15)

    # Put these two integers into data['params']
    data['params']['q'] = q
    data['params']['r'] = r

def grade(data):
    q = data['params']['q']
    r = data['params']['r']
    n = data['submitted_answers']['n']
    d = data['submitted_answers']['d']
    
    if divmod(n,d) == (q,r):
        data['score'] = 1
    else:
        data['score'] = 0