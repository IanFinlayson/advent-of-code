
# this is the reversed form of the goal program
seq = [0, 3, 5, 5, 1, 4, 3, 0, 5, 1, 5, 7, 3, 1, 4, 2]

# just returns the NEXT thing to be printed
# this is a dis-assembled version of my program
def formula(a):
    b = a & 7
    b = b ^ 3
    c = a >> b
    b = b ^ 5
    a = a >> 3
    b = b ^ c
    return b & 7

def check(a, goal):
    return formula(a) == goal

def toBin(num, limit):
    def bits(num):
        if num == 0:
            return ""
        else:
            return bits(num // 2) + str(num % 2)
    b = bits(num)
    while len(b) < limit:
        b = "0" + b
    return b

def toDecimal(binary):
    num = 0
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == "1":
            num += (2 ** (len(binary) - (i+1)))
    return num

def getOcts():
    octs = []
    return octs

# the sequence can start with an upper 6-bits or 64 diff things that have an effect
def getStarters():
    starters = []
    for i in range(2 ** 6):
        starters.append(toBin(i, 6))
    return starters

# ok now let's generalize this
def checkThings(levelAbove, index):
    result = []
    for above in levelAbove:
        for o in getOcts():
            num = above + o
            if check(toDecimal(num), seq[index]):
                result.append(num)
    return result

c15 = checkThings(getStarters(), 0)
c14 = checkThings(c15, 1)
c13 = checkThings(c14, 2)
c12 = checkThings(c13, 3)
c11 = checkThings(c12, 4)
c10 = checkThings(c11, 5)
c9 = checkThings(c10, 6)
c8 = checkThings(c9, 7)
c7 = checkThings(c8, 8)
c6 = checkThings(c7, 9)
c5 = checkThings(c6, 10)
c4 = checkThings(c5, 11)
c3 = checkThings(c4, 12)
c2 = checkThings(c3, 13)
c1 = checkThings(c2, 14)
c0 = checkThings(c1, 15)

# convert them to decimal
options = list(map(toDecimal, c0))

# find the smallest
print(min(options))

