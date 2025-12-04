def getGrid():
    grid = []
    while True:
        try:
            grid.append([c for c in input()])
        except EOFError:
            return grid

# returns a cell in a grid (and . if out of bounds)
def getCell(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return '.'
    else:
        return grid[r][c]

def neighbors(grid, r, c):
    n = 0
    for rmod in range(-1, 2):
        for cmod in range(-1, 2):
            if rmod == 0 and cmod == 0:
                pass
            else:
                if getCell(grid, r + rmod, c + cmod) == '@':
                    n += 1
    return n


def countAccessible(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@' and neighbors(grid, r, c) < 4:
                count += 1
    return count

def main():
    grid = getGrid()
    acc = countAccessible(grid)
    print(acc)


main()

