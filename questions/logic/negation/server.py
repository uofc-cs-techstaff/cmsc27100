import random

def generate(data):

    # Create a list of question prompts and the corresponding answers
    scenarios = [
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\wedge \\exists y Q(y))",
            "answer": "\\exists x (P(x) \\vee \\forall y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\wedge \\exists y Q(y))",
            "answer": "\\forall x (P(x) \\vee \\forall y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\wedge \\forall y Q(y))",
            "answer": "\\exists x (P(x) \\vee \\exists y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\wedge \\forall y Q(y))",
            "answer": "\\forall x (P(x) \\vee \\exists y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\vee \\exists y Q(y))",
            "answer": "\\exists x (P(x) \\wedge \\forall y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\vee \\exists y Q(y))",
            "answer": "\\forall x (P(x) \\wedge \\forall y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\vee \\forall y Q(y))",
            "answer": "\\exists x (P(x) \\wedge \\exists y \\neg Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\vee \\forall y Q(y))",
            "answer": "\\forall x (P(x) \\wedge \\exists y \\neg Q(y))",
        },
        
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\wedge \\exists y \\neg Q(y))",
            "answer": "\\exists x (P(x) \\vee \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\wedge \\exists y \\neg Q(y))",
            "answer": "\\forall x (P(x) \\vee \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\wedge \\forall y \\neg Q(y))",
            "answer": "\\exists x (P(x) \\vee \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\wedge \\forall y \\neg Q(y))",
            "answer": "\\forall x (P(x) \\vee \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\vee \\exists y \\neg Q(y))",
            "answer": "\\exists x (P(x) \\wedge \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\vee \\exists y \\neg Q(y))",
            "answer": "\\forall x (P(x) \\wedge \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (\\neg P(x) \\vee \\forall y \\neg Q(y))",
            "answer": "\\exists x (P(x) \\wedge \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (\\neg P(x) \\vee \\forall y \\neg Q(y))",
            "answer": "\\forall x (P(x) \\wedge \\exists y Q(y))",
        },
        
        {
            "statement": "\\neg \\forall x (P(x) \\wedge \\exists y \\neg Q(y))",
            "answer": "\\exists x (\\neg P(x) \\vee \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (P(x) \\wedge \\exists y \\neg Q(y))",
            "answer": "\\forall x (\\neg P(x) \\vee \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (P(x) \\wedge \\forall y \\neg Q(y))",
            "answer": "\\exists x (\\neg P(x) \\vee \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (P(x) \\wedge \\forall y \\neg Q(y))",
            "answer": "\\forall x (\\neg P(x) \\vee \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (P(x) \\vee \\exists y \\neg Q(y))",
            "answer": "\\exists x (\\neg P(x) \\wedge \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (P(x) \\vee \\exists y \\neg Q(y))",
            "answer": "\\forall x (\\neg P(x) \\wedge \\forall y Q(y))",
        },
        {
            "statement": "\\neg \\forall x (P(x) \\vee \\forall y \\neg Q(y))",
            "answer": "\\exists x (\\neg P(x) \\wedge \\exists y Q(y))",
        },
        {
            "statement": "\\neg \\exists x (P(x) \\vee \\forall y \\neg Q(y))",
            "answer": "\\forall x (\\neg P(x) \\wedge \\exists y Q(y))",
        },
    ]
    
    # Randomize the order of the scenarios
    random.shuffle(scenarios)

    # First shuffled scenario is the one we will take as correct
    data['params']['statement'] = scenarios[0]['statement']
    data['params']['correct_answer'] = scenarios[0]['answer']

    # Next three shuffled scenarios are the distractors
    data['params']['wrong_answer1'] = scenarios[1]["answer"]
    data['params']['wrong_answer2'] = scenarios[2]["answer"]
    data['params']['wrong_answer3'] = scenarios[3]["answer"]
