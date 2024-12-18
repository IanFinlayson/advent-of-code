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

def p(grid):
    for row in grid:
        for thing in row:
            if thing == None:
                print("[]", end="")
            elif thing < 10:
                print("0" + str(thing), end="")
            else:
                print(thing, end="")
        print()

# return spot in grid, or 0 if off map (that simulates byte already off edges so bounds checks easy)
def get(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0
    return grid[row][col]

# do the search thingy
def dijkstra(grid, size):
    # the tentative costs are a dict of (row, col, steps) keys and int values
    # if there is no path found, there is no entry
    tentative = dict()
    tentative[(0, 0, 0)] = 0

    # we make a heap of (row, col) to explore from
    nodes = []
    heapq.heappush(nodes, (0, 0, 0))

    while len(nodes) > 0:
        nrow, ncol, nsteps = heapq.heappop(nodes)
        print("\nConsidering", nrow, ncol, nsteps)
        if nsteps > size:
            continue

        # see where we can go from here TODO change >= to > maybe?
        options = []
        if get(grid, nrow - 1, ncol) == None or get(grid, nrow - 1, ncol) >= nsteps:
            options.append((nrow - 1, ncol))
        if get(grid, nrow + 1, ncol) == None or get(grid, nrow + 1, ncol) >= nsteps:
            options.append((nrow + 1, ncol))
        if get(grid, nrow, ncol - 1) == None or get(grid, nrow, ncol - 1) >= nsteps:
            options.append((nrow, ncol - 1))
        if get(grid, nrow, ncol + 1) == None or get(grid, nrow, ncol + 1) >= nsteps:
            options.append((nrow, ncol + 1))
        
        for drow, dcol in options:
            distance = tentative[(nrow, ncol, nsteps)] + 1
            if (drow, dcol, nsteps + 1) not in tentative or distance < tentative[(drow, dcol, nsteps + 1)]:
                tentative[(drow, dcol, nsteps + 1)] = distance
                heapq.heappush(nodes, (drow, dcol, nsteps + 1))

    # find thing in dict with lest steps to (size-1, size-1)
    best = None
    for (row, col, steps) in tentative:
        if row == size-1 and col == size-1:
            if best == None or steps < best:
                best = steps
    return steps


grid = getInput()
p(grid)
steps = dijkstra(grid, len(grid))
print(steps)



