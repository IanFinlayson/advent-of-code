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
# also keep track of directions for part 2
def walk(grid, row, col, direction, dirs):
    obstacles = []

    while True:
        # for part 2, we first record the direction we are travelling in
        dirs[row][col].add(direction)

        # TODO see if an obstacle would help here...

        # what cell is ahead of us?
        nrow, ncol = next(row, col, direction)
        n = get(grid, nrow, ncol)

        # if they are off map, wel'll be done
        if n == None:
            grid[row][col] = "X"
            return obstacles

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
row, col = startpos(grid)
print("Start:", row+1, col+1)

# for part 2 we also keep track of the directions we have traversed this cell in
# this is a set of the characters ^ < > v
dirs = [[set() for i in range(len(grid[0]))] for j in range(len(grid))]
obstacles = walk(grid, row, col, "^", dirs)

for row in dirs:
    for thing in row:
        num = 0
        if "^" in thing: num += 1
        if "v" in thing: num += 2
        if "<" in thing: num += 4
        if ">" in thing: num += 8
        print(hex(num)[2:], end="")
    print()
for row in grid:
    for thing in row:
        print(thing, end="")
    print()

for (a,b) in obstacles:
    print(a+1, b+1)

print(countX(grid))
