
def getInput():
    grid = []
    while True:
        try:
            grid.append(input())
        except EOFError:
            return grid

# returns a complete number in a cell, or None
# the number is represented as (row, (start, end))
def getNum(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return None
    elif not grid[r][c].isdigit():
        return None
    else:
        start = c
        while start > 0 and grid[r][start - 1].isdigit():
            start -= 1
        end = c
        while end < (len(grid[0]) - 1) and grid[r][end + 1].isdigit():
            end += 1
        return (r, (start, end))


def adjacentNums(grid, r, c):
    # we do it as a set at first to remove duplicates
    nums = set()
    adjs = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    for adj in adjs:
        n = getNum(grid, adj[0], adj[1])
        if n != None:
            nums.add(n)
    return list(nums)

def findGears(grid):
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '*':
                adjacent = adjacentNums(grid, r, c)
                if len(adjacent) == 2:
                    rowa, psa = adjacent[0]
                    rowb, psb = adjacent[1]
                    
                    vala = int(grid[rowa][psa[0]:psa[1] + 1])
                    valb = int(grid[rowb][psb[0]:psb[1] + 1])
                    total += vala * valb
    return total

grid = getInput()
print(findGears(grid))


