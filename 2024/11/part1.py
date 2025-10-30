import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    with open(sys.argv[1]) as file:
        return list(map(int, file.read().split()))

# this will surely not be enough, but let's try
def step(stones):
    toadd = []
    for i in range(len(stones)):
        s = str(stones[i])
        if stones[i] == 0:
            stones[i] = 1
        elif len(s) % 2 == 0:
            stones[i] = int(s[:len(s)//2])
            other = int(s[len(s)//2:])
            toadd.append((i + 1, other))
        else:
            stones[i] *= 2024

    for (i, new) in toadd:
        stones.insert(i, new)



stones = getInput()

for i in range(25):
    step(stones)

print(len(stones))

