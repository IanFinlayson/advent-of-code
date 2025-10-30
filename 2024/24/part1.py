import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    part1 = True
    wires = dict()
    gates = []
    with open(sys.argv[1]) as file:
        for line in file:
            if len(line) < 2:
                part1 = False
            elif part1:
                name, value = line.split(": ")
                wires[name] = int(value)
            else:
                parts = line.split()
                gates.append((parts[1], parts[0], parts[2], parts[4]))
    return wires, gates

def binOp(op, in1, in2):
    if op == "AND":
        return in1 & in2
    elif op == "OR":
        return in1 | in2
    elif op == "XOR":
        return in1 ^ in2
    else:
        print("Waaha this should not happen")

# evaluate all the gates, based on the wires we have got
def evalGates(wires, gates):
    while len(gates) > 0:
        for i in range(len(gates)):
            op, in1, in2, dest = gates[i]

            if in1 in wires and in2 in wires:
                wires[dest] = binOp(op, wires[in1], wires[in2])
                del gates[i]
                break

# get the number made up with all the 'z' wires
def part1(wires):
    val = 0
    for i in range(100):
        if i < 10:
            name = "z0" + str(i)
        else:
            name = "z" + str(i)
        
        if name not in wires:
            break
        else:
            val += wires[name] << i
    return val


wires, gates = getInput()
print(wires)
print(gates)

evalGates(wires, gates)
print(wires)

print(part1(wires))

