import sys
import random

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

def getOP(op):
    if op == "AND":
        return " & "
    elif op == "OR":
        return " | "
    elif op == "XOR":
        return " ^ "
    else:
        print("rutro -- bad operator")

# get a boolean expression for a specific wire in the system
def getExpression(wire, wires, gates):
    # if it's in the initial values, it's straight up
    if wire in wires:
        return wire

    # find the gate which produces this
    for gate in gates:
        if gate[3] == wire:
            return "(" + getExpression(gate[1], wires, gates) + getOP(gate[0]) + getExpression(gate[2], wires, gates) + ")"

    # we should not get here
    print("Wire", wire, "has no expression producing it")


## this was when I was hoping the expressions were systematically equivalent
## which doesn't seem to be the case (and checking if 2 exprs are equivalent is hard :\
def getAddExpr(a, b, cin):
    if cin == "0":
        return "(" + a + " ^ " + b + ")"
    else:
        return "(" + cin + ") ^ (" + a + " ^ " + b + ")"
def getCarryExpr(a, b, cin):
    if cin == "0":
        return "(" + a + " & " + b + ")"
    else:
        return "(" + a + " & " + b + " | ((" + a + " ^ " + b + ") & " + cin + "))"
def getSumExprs():
    zexprs = []
    carries = ["0"]
    for i in range(46):
        sum = getAddExpr("x" + numToStr(i), "y" + numToStr(i), carries[i])
        carry = getCarryExpr("x" + numToStr(i), "y" + numToStr(i), carries[i])
        zexprs.append(sum)
        carries.append(carry)
    return zexprs

def dumpExprs():
    wires, gates = getInput()
    mine = getSumExprs()
    for i in range(46):
        dest = "z" + numToStr(i)
        print(dest, "=", getExpression(dest, wires, gates))
        #print(dest, "=", mine[i])
        print()





# evaluate a boolean expression
def evalBoolean(expr, vars):
    for var in vars.keys():
        expr = expr.replace(var, str(vars[var]))
    return eval(expr)

def numToStr(num):
    if num < 10:
        return "0" + str(num)
    else:
        return str(num)

def getBits(num, letter, destDict):
    i = 0
    while num > 0:
        destDict[letter + numToStr(i)] = num % 2
        num = num // 2
        i += 1
    # put the next ones up in as 0
    for j in range(i, 46):
        destDict[letter + numToStr(j)] = 0

# test the system with a number
def test(x, y, exprs):
    # get the real answer
    vars = dict()
    xbits = getBits(x, "x", vars)
    ybits = getBits(y, "y", vars)
    
    answer = dict()
    zbits = getBits(x + y, "z", answer)
   
    # loop through and get the z vals
    for i in range(46):
        zgiven = evalBoolean(exprs[i], vars)
        if zgiven != answer["z" + numToStr(i)]:
            return i
    return None

def testNums(exprs, tests):
    first = None
    for i in range(tests):
        a = random.randint(0, 0xfffffffffff)
        b = random.randint(0, 0xfffffffffff)
        mistake = test(a, b, exprs)
        if mistake != None:
            if first == None or mistake < first:
                first = mistake
    print("First error found in bit position", first)

# this will detect mistakes in the adding circuit at a bit position
def detectMistake():
    wires, gates = getInput()

    exprs = []
    for i in range(46):
        name = "z" + numToStr(i)
        exprs.append(getExpression(name, wires, gates))
    testNums(exprs, 100)

#detectMistake()
dumpExprs()

