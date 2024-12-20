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
                heapq.heappush(nodes, (distance, drow, dcol))

    # find the cost to the end node
    return tentative[(end[0], end[1])]

def findPotentialCheats(grid):
    cheats = []
    # go horizontally through and find 1 or 2 # with . on either side
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if get(grid, row, col) != "#":
                if get(grid, row, col + 1) == "#" and get(grid, row, col + 2) != "#" or \
                   get(grid, row, col + 1) == "#" and get(grid, row, col + 2) == "#" and get(grid, row, col + 3) != "#":
                    cheats.append([(row, col + 1), (row, col + 2)])
    # now do the same but horizontally
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            if get(grid, row, col) != "#":
                if get(grid, row + 1, col) == "#" and get(grid, row + 2, col) != "#" or \
                   get(grid, row + 1, col) == "#" and get(grid, row + 2, col) == "#" and get(grid, row + 3, col) != "#":
                    cheats.append([(row + 1, col), (row + 2, col)])
    return cheats


def part1(grid):
    start = findSym(grid, "S")
    end = findSym(grid, "E")
    basescore = dijkstra(grid, start, end)
    
    cheats = findPotentialCheats(grid)
    count = 0
    i = 1
    for cheat in cheats:
        # save what used to be here, and mr gorbachev TEAR DOWN THIS WALL
        a = grid[cheat[0][0]][cheat[0][1]]
        b = grid[cheat[1][0]][cheat[1][1]]
        grid[cheat[0][0]][cheat[0][1]] = "."
        grid[cheat[1][0]][cheat[1][1]] = "."
       
        # check and see what the cost is now
        newscore = dijkstra(grid, start, end)
        if newscore <= (basescore - 100):
            count += 1
        
        # restore what used to be here
        grid[cheat[0][0]][cheat[0][1]] = a
        grid[cheat[1][0]][cheat[1][1]] = b
        print("Processed cheat", i, "out of", len(cheats))
        i += 1
    return count

grid = getInput()
count = part1(grid)
print(count)

