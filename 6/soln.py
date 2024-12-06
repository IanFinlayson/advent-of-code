import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    with open(sys.argv[1]) as file:
        for line in file:
            row = [let for let in line]
            grid.append(row[:-1])
    return grid

# return spot in grid based off coords or None if off map
def get(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    return grid[row][col]

def next(row, col, direction):
    match direction:
        case "^":
            return row - 1, col
        case "v":
            return row + 1, col
        case "<":
            return row, col - 1
        case ">":
            return row, col + 1

def rotate(direction):
    match direction:
        case "^":
            return ">"
        case "v":
            return "<"
        case "<":
            return "^"
        case ">":
            return "v"

# do the walking and put 'X' where they go
# return if there was a loop
def walk(grid, row, col, direction):
    # we keep track of states we've beein in before to check if we are in a loop
    history = [[set() for i in range(len(grid[0]))] for j in range(len(grid))]

    while True:
        # if we have been in this state, it's a loop!
        if direction in history[row][col]:
            return True

        # drop our breadcrumb
        history[row][col].add(direction)

        # what cell is ahead of us?
        nrow, ncol = next(row, col, direction)
        n = get(grid, nrow, ncol)

        # if they are off map, wel'll be done
        if n == None:
            grid[row][col] = "X"
            return False

        # if they are blocked, turn them
        if n == "#":
            direction = rotate(direction)
            continue
        
        # else put an X in old spot, and move them
        grid[row][col] = "X"
        row = nrow
        col = ncol

# in my input it was ^ so we look for just that
def startpos(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                return row, col

# part 1 answer
def countX(grid):
    count = 0
    for row in grid:
        for thing in row:
            if thing == "X":
                count += 1
    return count

grid = getInput()
startrow, startcol = startpos(grid)
print("Start:", startrow+1, startcol+1)

walk(grid, startrow, startcol, "^")

for row in grid:
    for thing in row:
        print(thing, end="")
    print()

print(countX(grid))

# part 2, consider each possible place to put an obstacle, then see if it makes a loop
def obstacles(grid):
    obs = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in ["-", "X"]:
                grid[row][col] = "#"
                if walk(grid, startrow, startcol, "^"):
                    obs.append((row, col))
                grid[row][col] = "-"
        print("Row", row, "done")
    return obs

obs = obstacles(grid)

print(obs)
print(len(obs))


