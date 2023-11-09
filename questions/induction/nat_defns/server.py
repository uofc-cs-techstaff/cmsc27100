import random

def generate(data):

    # Create a list of question prompts and the corresponding answers
    scenarios = [
        {
            "relation": "equal to",
            "notation": "m = n",
            "base" : "$m = z$ and $n = z$",
            "recursive" : "$m = \operatorname{succ}(k)$ and $n = \operatorname{succ}(\ell)$"
        },
        {
            "relation": "less than",
            "notation": "m \lt n",
            "base" : "$m = z$ and $n = \operatorname{succ}(\ell)$",
            "recursive" : "$m = \operatorname{succ}(k)$ and $n = \operatorname{succ}(\ell)$"
        },
        {
            "relation": "greater than",
            "notation": "m \gt n",
            "base" : "$m = \operatorname{succ}(k)$ and $n = z$",
            "recursive" : "$m = \operatorname{succ}(k)$ and $n = \operatorname{succ}(\ell)$"
        },
    ]
    
    cases = ["base", "recursive"]
    # Randomize the order of the scenarios
    random.shuffle(scenarios)
    random.shuffle(cases)
    
    # First shuffled scenario is the one we will take as correct
    data['params']['relation'] = scenarios[0]['relation']
    data['params']['notation'] = scenarios[0]['notation']
    data['params']['case'] = cases[0]
    data['params']['correct_answer'] = scenarios[0][cases[0]]

    # Next three shuffled scenarios are the distractors
    data['params']['wrong_answer1'] = scenarios[0][cases[1]]
    data['params']['wrong_answer2'] = scenarios[1]["base"]
    data['params']['wrong_answer3'] = scenarios[2]["base"]
