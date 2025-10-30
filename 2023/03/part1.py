
def getInput():
    grid = []
    while True:
        try:
            grid.append(input())
        except EOFError:
            return grid

def isPart(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    if grid[r][c].isdigit():
        return False
    if grid[r][c] == '.':
        return False
    return True

def adjacent(grid, r, c):
    if isPart(grid, r - 1, c - 1): return True
    if isPart(grid, r - 1, c): return True
    if isPart(grid, r - 1, c + 1): return True

    if isPart(grid, r, c - 1): return True
    if isPart(grid, r, c + 1): return True

    if isPart(grid, r + 1, c - 1): return True
    if isPart(grid, r + 1, c): return True
    if isPart(grid, r + 1, c + 1): return True
    return False

def getNumList(grid):
    nums = []

    # are we in a number, and is it adjacent to sth?
    innum = False
    adj = False
    numby = ""

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].isdigit():
                innum = True
                numby += grid[r][c]
                if adjacent(grid, r, c):
                    adj = True
            else:
                if innum and adj:
                    nums.append(int(numby))
                numby = ""
                innum = False
                adj = False
    return nums

grid = getInput()
nums = getNumList(grid)
print(sum(nums))


