import random, copy

def generate(data):

    l = random.randint(6, 16)
    rules = [
        "first initial, always a letter",
        "middle initial, a letter, if one exists",
        "followed by a dash",
        "possibly followed by a number from 1 to 999",
        "followed by ",
        "followed by ",
        "surname, possibly truncated if the entire username exceeds length " + str(l)
    ]
    a = random.choice(list(range(-m+1,-1)) + list(range(2,m)))
    b = random.randint(200,5000)
    


    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['m'] = m

    # Compute the sum of these two integers
    c = pow(a,b,m)

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
