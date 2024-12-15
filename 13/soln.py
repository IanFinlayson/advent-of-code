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
    px = int(l3[1])
    py = int(l3[2])
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
def getB(ax, ay, bx, by, px, py):
    num = (py/ay) - (px/ax)
    den = (by/ay) - (bx/ax)
    return num / den

# we can calculate A based on the value for B
def getA(ax, ay, bx, by, px, py, b):
    return (px - bx*b) / ax

# check if a number is pretty dang close to a whole number
def isWhole(num):
    whole = math.isclose(num, round(num))
    print(num, whole)
    return whole

def getCost(a, b):
    return 3*a + b

cost = 0
cases = getInput()
for t in cases:
    b = getB(t[0], t[1], t[2], t[3], t[4], t[5])
    a = getA(t[0], t[1], t[2], t[3], t[4], t[5], b)
    if isWhole(a) and isWhole(b):
        cost += getCost(a, b)
print(cost)

