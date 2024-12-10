import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    with open(sys.argv[1]) as file:
        for line in file:
            row = [int(num) for num in line[:-1]]
            grid.append(row)
    return grid

def p(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()

def cango(grid, r0, c0, r1, c1):
    if r1 < 0 or r1 >= len(grid) or c1 < 0 or c1 >= len(grid[0]):
        return False
    return grid[r1][c1] - grid[r0][c0] == 1

# find how many 9's we can reach from the trailhead
def dfsPart1(grid, row, col, visited):
    visited[row][col] = True
    summits = set()
    
    # if we hit a summit, return where
    if grid[row][col] == 9:
        return {(row, col)}

    # up
    if cango(grid, row, col, row - 1, col):
        summits = summits.union(dfsPart1(grid, row - 1, col, visited))
    # down
    if cango(grid, row, col, row + 1, col):
        summits = summits.union(dfsPart1(grid, row + 1, col, visited))
    # left
    if cango(grid, row, col, row, col - 1):
        summits = summits.union(dfsPart1(grid, row, col - 1, visited))
    # right
    if cango(grid, row, col, row, col + 1):
        summits = summits.union(dfsPart1(grid, row, col + 1, visited))

    return summits

# find how distinct trails to 9's we can reach from the trailhead
def dfsPart2(grid, row, col, visited, path):
    visited[row][col] = True
    summits = set()
    path2 = path + str((row, col))
    
    # if we hit a summit, return where
    if grid[row][col] == 9:
        return {path2}

    # up
    if cango(grid, row, col, row - 1, col):
        summits = summits.union(dfsPart2(grid, row - 1, col, visited, path2))
    # down
    if cango(grid, row, col, row + 1, col):
        summits = summits.union(dfsPart2(grid, row + 1, col, visited, path2))
    # left
    if cango(grid, row, col, row, col - 1):
        summits = summits.union(dfsPart2(grid, row, col - 1, visited, path2))
    # right
    if cango(grid, row, col, row, col + 1):
        summits = summits.union(dfsPart2(grid, row, col + 1, visited, path2))

    return summits

def findTrailheads(grid):
    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
                summits = dfsPart2(grid, row, col, visited, "")
                score += len(summits)
    return score

grid = getInput()
trailheads = findTrailheads(grid)
print(trailheads)

