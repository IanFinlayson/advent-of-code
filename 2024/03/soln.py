import sys
import re

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    prog = ""
    with open(sys.argv[1]) as file:
        for line in file:
            prog += line
    return prog

def evalatePart1(prog):
    total = 0
    things = re.findall("mul\((\d\d?\d?),(\d\d?\d?)\)", prog)
    for thing in things:
        total += int(thing[0]) * int(thing[1])
    return total


# we pre-process the program to remove dont'ed out parts
def evalatePart2(prog):
    # find locations of dos and donts
    cmds = []
    for cmd in re.finditer("don't\(\)", prog):
        cmds.append(("dont", cmd.start()))
    for cmd in re.finditer("do\(\)", prog):
        cmds.append(("do", cmd.start()))

    # sort by line number
    cmds.sort(key = lambda cmd: cmd[1])

    # loop through dos and donts and keep track of code
    on = True
    last = 0
    edited = ""
    for cmd in cmds:
        # if on, copy in part so far
        if on:
            edited += prog[last:cmd[1]]
        last = cmd[1]

        # turn off for a dont
        if cmd[0] == "dont":
            on = False

        # turn on for a do
        if cmd[0] == "do":
            on = True
    
    # if still on, copy in rest
    if on:
        edited += prog[last:]

    # now eval this
    return evalatePart1(edited)

prog = getInput()
total = evalatePart2(prog)
print(total)


