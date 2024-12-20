import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    prog = ""

    onCode = False
    with open(sys.argv[1]) as file:
        for line in file:
            if len(line) < 2:
                onCode = True
            elif onCode:
                prog = prog + line[:-1]
            else:
                row = []
                for sym in line[:-1]:
                    if sym == "#":
                        row.append("#")
                        row.append("#")
                    elif sym == "O":
                        row.append("[")
                        row.append("]")
                    elif sym == ".":
                        row.append(".")
                        row.append(".")
                    elif sym == "@":
                        row.append("@")
                        row.append(".")
                    else:
                        print("WAAAAAH this should not happen!")
                grid.append(row)
    return grid, prog

def p(grid):
    for row in grid:
        for thing in row:
            print(thing, end="")
        print()

# find the robot
def findbot(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                return row, col
    # should not happen
    return None

# only called when next thing is a box
def handleHorizontal(grid, row, col, colmod):
    boxes = 0
    while grid[row][col + (colmod * (boxes + 1))] in "[]":
        boxes += 1

    # see if the thing there is free
    if grid[row][col + (colmod * (boxes + 1))] == "#":
        return

    # do the move
    step = (boxes + 1)
    while step >= 0:
        grid[row][col + colmod * step] = grid[row][col + colmod * (step - 1)]
        step -= 1
    grid[row][col + colmod] = "@"

# check if we CAN do a vertical step or not
def canStepVerical(grid, row, col, rowmod):
    # easy cases
    if grid[row + rowmod][col] == ".":
        return True
    if grid[row + rowmod][col] == "#":
        return False
    # we just go up above and for the other one
    if grid[row + rowmod][col] == "[":
        return canStepVerical(grid, row + rowmod, col, rowmod) and canStepVerical(grid, row + rowmod, col + 1, rowmod)
    if grid[row + rowmod][col] == "]":
        return canStepVerical(grid, row + rowmod, col, rowmod) and canStepVerical(grid, row + rowmod, col - 1, rowmod)
    print("This should never happen")

# actually do the vertical step
def makeStepVertical(grid, row, col, rowmod):
    # TODO this is tricky, but all we have left
    pass
        

def move(grid, row, col, rowmod, colmod):
    # if the robot walks into a space, fine
    if grid[row + rowmod][col + colmod] == ".":
        grid[row][col] = "."
        grid[row + rowmod][col + colmod] = "@"
        return

    # if the robot walks into a wall, nothing happens
    if grid[row + rowmod][col + colmod] == "#":
        return

    # if the robot walks into a box...
    if grid[row + rowmod][col + colmod] in "[]":
        # the easy case first
        if rowmod == 0:
            handleHorizontal(grid, row, col, colmod)
        else:
            if canStepVerical(grid, row, col, rowmod):
                makeStepVertical(grid, row, col, rowmod)

# simulate just one step
def step(grid, dir):
    # find the relevant deets and do the move
    row, col = findbot(grid)
    rowmod = 0
    colmod = 0
    match dir:
        case "<":
            colmod = -1
        case ">":
            colmod = 1
        case "^":
            rowmod = -1
        case "v":
            rowmod = 1
    move(grid, row, col, rowmod, colmod)


# do the whole simulation
def sim(grid, prog):
    for dir in prog:
        step(grid, dir)


grid, prog = getInput()
#sim(grid, prog)
p(grid)

step(grid, "<")
step(grid, "^")
print("\n")
p(grid)

