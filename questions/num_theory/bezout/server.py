import random, copy, math

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    m = random.randint(2, 20)
    n = random.randint(1, 15)

    # Put these two integers into data['params']
    data['params']['m'] = m
    data['params']['n'] = n
    

def grade(data):
    m = data['params']['m']
    n = data['params']['n']
    a = data['submitted_answers']['a']
    b = data['submitted_answers']['b']
    c = data['submitted_answers']['c']
    
    if c == a*m + b*n and c != math.gcd(m,n):
        data['score'] = 1
    else:
        data['score'] = 0