import random, copy, math

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    d = random.randint(2,10)
    a = d * random.randint(1,11)
    b = d * random.randint(1,9)
    
    while math.gcd(a,b) == 1 or a % b == 0 or b % a == 0:
        a = d * random.randint(1,11)
        b = d * random.randint(1,9)
    

    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['corr'] = math.gcd(a,b)


def grade(data):
    c = data["submitted_answers"]['c']
    a = data['params']['a']
    b = data['params']['b']
    if a % c == 0 and b % c == 0 and c > 1:
        data["score"] = 1
    else:
        data["score"] = 0