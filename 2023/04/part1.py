import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    with open(sys.argv[1]) as file:
        cases = []
        for line in file:
            things = line.split()
            winning = []
            mine = []
            seenbar = False
            for thing in things[2:]:
                if thing == "|":
                    seenbar = True
                elif seenbar:
                    mine.append(int(thing))
                else:
                    winning.append(int(thing))
            cases.append((winning, mine))
    return cases

def inc(score):
    if score == 0:
        return 1
    else:
        return score * 2

def process(thecase):
    winning = thecase[0]
    mine = thecase[1]
    score = 0
    for num in mine:
        if num in winning:
            score = inc(score)
    return score

cases = getInput()
total = 0
for thecase in cases:
    total += process(thecase)
print(total)

