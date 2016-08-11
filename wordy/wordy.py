import operator
import sys
def calculate(problem):
    print problem
    outcome = 0
    operators = []
    operants = []
    ops = { "plus": operator.add,
            "minus": operator.sub,
            "multiplied by": operator.mul,
            "divided by": operator.div}
    parts = [str(x) for x in problem.split(' ')];
    for part in parts:
        if part == "multiplied":
            operators.append("multiplied by")
        elif part == "divided":
            operators.append("divided by")
        elif part == "plus":
            operators.append("plus")
        elif part == "minus":
            operators.append("minus")
        elif RepresentsInt(part):
            operants.append(int(part))
        elif part[-1:] == "?":
            part = part[:-1]
            operants.append(int(part))
    print operators
    print operants
    if (len(operators)+1 != len(operants)):
        raise ValueError
    outcome = operants[0]
    for index in range(len(operators)):
        op_func = ops[operators[index]]
        outcome = op_func(outcome,operants[index+1])
    return outcome

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
