import random, copy

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    b = random.randint(5, 15)
    a = random.choice(list(range(-100,-b)) + list(range(b,200)))


    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b

    # Compute the sum of these two integers
    c = a % b

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
