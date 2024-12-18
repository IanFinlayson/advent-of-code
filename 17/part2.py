import sys

# for part 2 we'll try the dubious approach of simming the cpu w/ different a values
# we bail after a certain number of steps.  This *probably* won't work, but the alternative seems very hard
MAX_STEPS = 1000

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    prog = ""
    with open(sys.argv[1]) as file:
        a = int(file.readline()[12:])
        b = int(file.readline()[12:])
        c = int(file.readline()[12:])
        file.readline()
        prog = list(map(int, file.readline()[9:].split(",")))
    return a, b, c, prog

# a machine state is a tuple of (a, b, c, ip)
# this function takes a machine state and program and returns next machine state, or None if done
def cycle(state, prog, output):
    a, b, c, ip = state
    
    # if the ip out of bounds, we halt
    if ip >= len(prog):
        return None

    # get the opcode and operand
    opcode = prog[ip]
    operand = prog[ip + 1]
    if operand < 4:
        combo = operand
    elif operand == 4:
        combo = a
    elif operand == 5:
        combo = b
    elif operand == 6:
        combo = c
    else:
        print("This supposedly should never happen!")

    # do the thing
    match opcode:
        case 0:
            a = a // (2 ** combo)
            ip += 2
        case 1:
            b = b ^ operand
            ip += 2
        case 2:
            b = combo % 8
            ip += 2
        case 3:
            if a == 0:
                ip += 2
            else:
                ip = operand
        case 4:
            b = b ^ c
            ip += 2
        case 5:
            output.append(combo % 8)
            ip += 2
        case 6:
            b = a // (2 ** combo)
            ip += 2
        case 7:
            c = a // (2 ** combo)
            ip += 2
    return a, b, c, ip

def findA(origb, origc, prog):
    for a in range(100000000):
        state = a, origb, origc, 0
        step = 0

        output = []
        while state != None and step < MAX_STEPS:
            state = cycle(state, prog, output)

        #print("\n", output)
        #print(prog)

        if state != None:
            print("andoned")
            pass
        else:
            if output == prog:
                #print("Done and found it!!!")
                return a
            else:
                #print("done and no.")
                pass
    return None


a, b, c, prog = getInput()
a = findA(b, c, prog)
print(a)

