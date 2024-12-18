import sys
import heapq

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    with open(sys.argv[1]) as file:
        i = 0
        for line in file:
            if i == 0:
                size = int(line)
                grid = [[None for i in range(size)] for j in range(size)]
            else:
                col, row = tuple(map(int, line.split(",")))
                grid[row][col] = i
            i += 1
    return grid

def p(grid, fallen):
    for row in grid:
        for thing in row:
            if thing == None:
                print(".", end="")
            elif thing <= fallen:
                print("#", end="")
            else:
                print(".", end="")
        print()

# return spot in grid, or 0 if off map (that simulates byte already off edges so bounds checks easy)
def get(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0
    return grid[row][col]

# do the search thingy
def dijkstra(grid, size, fallen):
    # the tentative costs are a dict of (row, cols) keys and int values
    # if there is no path found, there is no entry
    tentative = dict()
    tentative[(0, 0)] = 0

    # we make a heap of (steps, row, col) to explore from
    nodes = []
    heapq.heappush(nodes, (0, 0, 0))

    while len(nodes) > 0:
        nsteps, nrow, ncol = heapq.heappop(nodes)
        #print("\nConsidering", nrow, ncol)

        options = []
        if get(grid, nrow - 1, ncol) == None or get(grid, nrow - 1, ncol) > fallen:
            options.append((nrow - 1, ncol))
        if get(grid, nrow + 1, ncol) == None or get(grid, nrow + 1, ncol) > fallen:
            options.append((nrow + 1, ncol))
        if get(grid, nrow, ncol - 1) == None or get(grid, nrow, ncol - 1) > fallen:
            options.append((nrow, ncol - 1))
        if get(grid, nrow, ncol + 1) == None or get(grid, nrow, ncol + 1) > fallen:
            options.append((nrow, ncol + 1))
        
        for drow, dcol in options:
            distance = tentative[(nrow, ncol)] + 1
            if (drow, dcol) not in tentative or distance < tentative[(drow, dcol)]:
                tentative[(drow, dcol)] = distance
                heapq.heappush(nodes, (distance, drow, dcol))

    # find thing in dict with lest steps to (size-1, size-1)
    if (size - 1, size - 1) in tentative:
        return tentative[(size - 1, size - 1)]
    else:
        return None

def findLastByte(grid, size):
    fallen = 0
    while True:
        steps = dijkstra(grid, len(grid), fallen)
        if steps == None:
            break
        fallen += 1

    # find the one with this index
    for row in range(size):
        for col in range(size):
            if grid[row][col] == fallen:
                return col, row

grid = getInput()
print(findLastByte(grid, len(grid)))

