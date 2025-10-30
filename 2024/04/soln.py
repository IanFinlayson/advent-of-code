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

# we use this to lookup char from grid, invalid indices give '-' instead of exception
def lett(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return '-'
    return grid[row][col]

# recursive search in a direction
def searchDir(grid, row, col, rowmod, colmod, i):
    # check next one in sequence
    if lett(grid, row + rowmod, col + colmod) == "XMAS"[i + 1]:
        if i == 2:
            return 1
        else:
            # keep truckin
            return searchDir(grid, row + rowmod, col + colmod, rowmod, colmod, i + 1)
    else:
        return 0

# search in all directions
def search(grid, row, col):
    count = 0
    count += searchDir(grid, row, col, -1, -1, 0) # NW
    count += searchDir(grid, row, col, -1,  0, 0) # N
    count += searchDir(grid, row, col, -1, +1, 0) # NE
    count += searchDir(grid, row, col,  0, -1, 0) # W
    count += searchDir(grid, row, col,  0, +1, 0) # E
    count += searchDir(grid, row, col, +1, -1, 0) # SW
    count += searchDir(grid, row, col, +1,  0, 0) # S
    count += searchDir(grid, row, col, +1, +1, 0) # SE
    return count

# look through whole grid for X's to start search at
def findXMASpart1(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                count += search(grid, row, col)
    return count

def findXMASpart2(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'A':
                # check \ part, then / part
                if lett(grid, row - 1, col - 1) + lett(grid, row + 1, col + 1) in ["SM", "MS"] and \
                   lett(grid, row + 1, col - 1) + lett(grid, row - 1, col + 1) in ["SM", "MS"]:
                       count += 1
    return count

grid = getInput()
count = findXMASpart2(grid)
print(count)

