import sys
import math

# I didn't want to parse the file, so I cheated and re-formatted it in vim :)
def getCase(file):
    l1 = file.readline().split()
    l2 = file.readline().split()
    l3 = file.readline().split()
    ax = int(l1[1])
    ay = int(l1[2])
    bx = int(l2[1])
    by = int(l2[2])
    # add the huge number for part 2
    px = int(l3[1]) + 10000000000000
    py = int(l3[2]) + 10000000000000
    return ax, ay, bx, by, px, py

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    cases = []
    with open(sys.argv[1]) as file:
        num = int(file.readline())
        for i in range(num):
            cases.append(getCase(file))
    return cases

# we calculate B based on a buncha math
# re-done for par 2 to use integers only
def getB(ax, ay, bx, by, px, py):
    num = py*ax - px*ay
    denom = by*ax - bx*ay

    if num % denom == 0:
        return num // denom
    else:
        return None

# we can calculate A based on the value for B
def getA(ax, ay, bx, by, px, py, b):
    if (px - bx*b) % ax == 0:
        return (px - bx*b) // ax
    else:
        return None

def getCost(a, b):
    return 3*a + b

cost = 0
cases = getInput()
i = 0
for t in cases:
    b = getB(t[0], t[1], t[2], t[3], t[4], t[5])
    if b != None:
        a = getA(t[0], t[1], t[2], t[3], t[4], t[5], b)
        if a != None:
            print("can get", i)
            print(a, b)
            cost += getCost(a, b)
    i += 1
print(cost)

