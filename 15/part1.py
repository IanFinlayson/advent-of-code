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
                grid.append([let for let in line[:-1]])
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
    if grid[row + rowmod][col + colmod] == "O":
        # scan for the next non-box after the box
        boxes = 1
        while grid[row + rowmod*boxes][col + colmod*boxes] == "O":
            boxes += 1

        # if it's a wall, nothing happens
        if grid[row + rowmod*boxes][col + colmod*boxes] == "#":
            return
        else:
            # shift them down
            grid[row + rowmod*boxes][col + colmod*boxes] = "O"
            grid[row][col] = "."
            grid[row + rowmod][col + colmod] = "@"
            return


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


# calculate the part 1 score
def calcScore(grid):
    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "O":
                score += 100*row + col
    return score

grid, prog = getInput()
sim(grid, prog)
p(grid)

print(calcScore(grid))

