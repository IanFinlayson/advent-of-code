import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    with open(sys.argv[1]) as file:
        return list(map(int, file.read().split()))

# we compute the next stone(s) from one
def next(stone):
    s = str(stone)
    if stone == 0:
        return [1]
    elif len(s) % 2 == 0:
        a = int(s[:len(s)//2])
        b = int(s[len(s)//2:])
        return [a, b]
    else:
        return [stone * 2024]

# we memoize the fanout based on the stone value/blinks pair
table = dict()

# recursively compute the number of stones produced from one after certain blinks
def fanout(stone, blinks):
    # check if this result is memoized
    if (stone, blinks) in table:
        return table[(stone, blinks)]

    if blinks == 0:
        return 1
    else:
        # get the result and memoize it
        result = sum([fanout(child, blinks - 1) for child in next(stone)])
        table[(stone, blinks)] = result
        return result

stones = getInput()
count = 0
for stone in stones:
    count += fanout(stone, 75)
print(count)


