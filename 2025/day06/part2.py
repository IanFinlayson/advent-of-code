from functools import reduce

def getProbs():
    lines = []
    while True:
        try:
            # we add a blank space to each line to simplify logic below
            lines.append(input() + ' ')
        except EOFError:
            break

    probs = []
    current = []

    # for each column of text
    for col in range(len(lines[0])):
        num = ""

        # for each row of the text except the last
        for row in range(len(lines) - 1):
            if lines[row][col] != ' ':
                num += lines[row][col]

        if num != "":
            # add this number to current problem
            current.append(int(num))
        else:
            # add this problem to list of problems
            probs.append(current)
            current = []

    ops = lines[-1].split()
    result = []
    for i in range(len(probs)):
        result.append((probs[i], ops[i]))
    return result


def main():
    probs = getProbs()
    total = 0
    for prob in probs:
        if prob[1] == '+':
            total += sum(prob[0])
        else:
            total += reduce(lambda a, b: a * b, prob[0], 1)
    print(total)


main()


