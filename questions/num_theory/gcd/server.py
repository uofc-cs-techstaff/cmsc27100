import random, copy, math

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(10, 100)
    b = random.randint(5, 20)

    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = math.gcd(a,b)
