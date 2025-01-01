import sys
import random

# in this approach, we will re-write the input file to be more readable...

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    part1 = True
    gates = []
    with open(sys.argv[1]) as file:
        for line in file:
            if len(line) < 2:
                part1 = False
            elif not part1:
                parts = line.split()
                gates.append((parts[1], parts[0], parts[2], parts[4]))
    return gates

# always put the x part on the left
def swapXY(gates):
    for i in range(len(gates)):
        g = gates[i]
        if g[1][0] == "y" and g[2][0] == "x":
            gates[i] = (g[0], g[2], g[1], g[3])

# always put the G or P part on the left:
def swapGP(gates):
    for i in range(len(gates)):
        g = gates[i]
        if g[2][0] == "g" and g[2][1:].isdigit() or g[2][0] == "p" and g[2][1:].isdigit():
            gates[i] = (g[0], g[2], g[1], g[3])

def replaceWire(gates, a, b):
    print("Renaming", a, "to", b)
    for i in range(len(gates)):
        g = gates[i]
        new = [g[0], g[1], g[2], g[3]]
        if g[0] == a:
            new[0] = b
        if g[1] == a:
            new[1] = b
        if g[2] == a:
            new[2] = b
        if g[3] == a:
            new[3] = b
        gates[i] = tuple(new)

# rename the xi ^ yi gates to be si
def identifySums(gates):
    reps = []
    # find them all first
    for i in range(len(gates)):
        g = gates[i]
        if g[1][0] == "x" and g[2][0] == "y" and g[0] == "XOR":
            reps.append((g[3], "p" + g[1][1:]))
    # replace them all
    for rep in reps:
        replaceWire(gates, rep[0], rep[1])

def identifyCarries(gates):
    reps = []
    # find them all first
    for i in range(len(gates)):
        g = gates[i]
        if g[1][0] == "x" and g[2][0] == "y" and g[0] == "AND":
            reps.append((g[3], "g" + g[1][1:]))
    # replace them all
    for rep in reps:
        replaceWire(gates, rep[0], rep[1])

def identifyTemps(gates):
    reps = []
    for i in range(len(gates)):
        g = gates[i]
        if g[1][0] == "p" and g[0] == "AND":
            reps.append((g[3], "t" + g[1][1:]))
    # replace them all
    for rep in reps:
        replaceWire(gates, rep[0], rep[1])

def identifyChains(gates):
    reps = []
    for i in range(len(gates)):
        g = gates[i]
        if g[1][0] == "g" and g[0] == "OR":
            reps.append((g[3], "c" + g[1][1:]))
    # replace them all
    for rep in reps:
        replaceWire(gates, rep[0], rep[1])

def dump(gates):
    last = -1
    for gate in gates:
        if gate[3][1:].isdigit():
            if last == -1 or last != int(gate[3][1:]):
                print()
                last = int(gate[3][1:])
        print(gate[1], gate[0], gate[2], "->", gate[3])

def score(gate):
    op, in1, in2, out = gate
    
    # put all the non-fixed ones last
    if not out[1:].isdigit():
        return 0

    s = int(out[1:]) * 1000
    if out[0] == "p":
        s += 0
    elif out[0] == "g":
        s += 1
    elif out[0] == "t":
        s += 2
    elif out[0] == "c":
        s += 3
    elif out[0] == "z":
        s ++ 4
    return s

gates = getInput()
swapXY(gates)
identifySums(gates)
identifyCarries(gates)
swapGP(gates)

identifyTemps(gates)
identifyChains(gates)

gates.sort(key = score)
dump(gates)



