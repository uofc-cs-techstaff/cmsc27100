import random, copy, math

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    n = random.randint(10, 999)
    d = random.randint(5, 99)

    # Put these two integers into data['params']
    data['params']['n'] = n
    data['params']['d'] = d

def grade(data):
    n = data['params']['n']
    d = data['params']['d']
    r = data['submitted_answers']['r']
    
    if (n-r)%d == 0:
        data['score'] = 1
    else:
        data['score'] = 0