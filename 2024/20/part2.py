import heapq
import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    with open(sys.argv[1]) as file:
        for line in file:
            grid.append([let for let in line[:-1]])
    return grid

def get(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return "#"
    else:
        return grid[row][col]

def p(grid):
    for row in grid:
        for thing in row:
            print(thing, end="")
        print()

# find the start/end
def findSym(grid, sym):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == sym:
                return row, col
    # should not happen
    return None

# do the search thingy
def dijkstra(grid, start, end):
    # the tentative costs are a dict of (row, col, dir) keys and int values
    # if there is no path found, there is no entry
    tentative = dict()
    tentative[(start[0], start[1])] = 0
    
    path = dict()
    path[(start[0], start[1])] = [(start[0], start[1])]

    # we make a heap of (cost, row, col) to explore from
    nodes = []
    heapq.heappush(nodes, (0, start[0], start[1]))

    while len(nodes) > 0:
        tent, nrow, ncol = heapq.heappop(nodes)

        # see where we can go from 
        possibles = []
        if get(grid, nrow - 1, ncol) != "#":
            possibles.append((nrow - 1, ncol))
        if get(grid, nrow + 1, ncol) != "#":
            possibles.append((nrow + 1, ncol))
        if get(grid, nrow, ncol - 1) != "#":
            possibles.append((nrow, ncol - 1))
        if get(grid, nrow, ncol + 1) != "#":
            possibles.append((nrow, ncol + 1))
        
        # try to go each place
        for (drow, dcol) in possibles:
            distance = tentative[(nrow, ncol)] + 1

            if (drow, dcol) not in tentative or distance < tentative[(drow, dcol)]:
                tentative[(drow, dcol)] = distance
                path[(drow, dcol)] = path[(nrow, ncol)] + [(drow, dcol)]
                heapq.heappush(nodes, (distance, drow, dcol))

    # find the cost to the end node
    return tentative[(end[0], end[1])], path[(end[0], end[1])]

def cartesianDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part2(grid, start, end):
    # we are now interested in the path itself
    score, path = dijkstra(grid, start, end)
   
    # we now go through every pair of cells on the path
    count = 0
    for start in range(len(path) - 1):
        for end in range(start + 1, len(path)):
            # how far away if we are cheating
            direct = cartesianDistance(path[start], path[end])
            
            # how far away if we follow the path
            indirect = end - start

            # if direct within range AND savings at least 100
            if direct <= 20 and (indirect - direct) >= 100:
                count += 1
    return count


grid = getInput()
start = findSym(grid, "S")
end = findSym(grid, "E")
count = part2(grid, start, end)
print(count)


