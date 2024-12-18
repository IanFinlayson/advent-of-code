import sys

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
def cycle(state, prog):
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
            print(str(combo % 8), end=",")
            ip += 2
        case 6:
            b = a // (2 ** combo)
            ip += 2
        case 7:
            c = a // (2 ** combo)
            ip += 2
    return a, b, c, ip

a, b, c, prog = getInput()
state = a, b, c, 0

while state != None:
    state = cycle(state, prog)

print()

