from functools import reduce

def getProbs():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    problems = [[] for i in range(len(lines[0].split()))]
    for line in lines[:-1]:
        nums = list(map(int, line.split()))
        for i in range(len(nums)):
            problems[i].append(nums[i])
    
    ops = lines[-1].split()
    result = []
    for i in range(len(problems)):
        result.append((problems[i], ops[i]))
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


