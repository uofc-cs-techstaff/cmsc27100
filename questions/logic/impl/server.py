import numpy
import sympy

def generate(data):

    # Randomize the number of variables
    tf = numpy.random.choice([True,False])
    
    # Modify data and return
    if tf:
        data["params"]["t"] = "true"
        data["params"]["f"] = "false"
        data["params"]["not"] = ""
    else:
        data["params"]["t"] = "false"
        data["params"]["f"] = "true"
        data["params"]["not"] = "not"

if __name__ == "__main__":
    generate({"params":{}})
