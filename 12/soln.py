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


def floodID(crop, grid, regions, row, col, id):
    # if out of bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return

    # if we've been here before
    if regions[row][col] != -1:
        return

    # if it's not the crop we're looking for
    if grid[row][col] != crop:
        return

    # mark it and recurse out
    regions[row][col] = id
    floodID(crop, grid, regions, row - 1, col, id)
    floodID(crop, grid, regions, row + 1, col, id)
    floodID(crop, grid, regions, row, col - 1, id)
    floodID(crop, grid, regions, row, col + 1, id)

# replaces letters with region ids, 0+
def findRegions(grid):
    regions = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    symbols = []
    nextrow, nextcol = 0, 0
    nextid = 0
    done = False

    while not done:
        # flood fill nextrow, nextcol
        floodID(grid[nextrow][nextcol], grid, regions, nextrow, nextcol, nextid)
        symbols.append(grid[nextrow][nextcol])

        # get next stuff
        isNext = False
        for row in range(0, len(grid)):
            if isNext:
                break
            for col in range(0, len(grid[0])):
                if isNext:
                    break
                if regions[row][col] == -1:
                    nextrow = row
                    nextcol = col
                    isNext = True
            
        # check if done
        if not isNext:
            done = True
        else:
            nextid += 1
    return regions, nextid + 1, symbols

# returns -1 for out-of-bounds to simplify checks
def r(regions, row, col):
    if row < 0 or row >= len(regions) or col < 0 or col >= len(regions[0]):
        return -1
    return regions[row][col]

def part1(regions, num):
    # the regions each have a slot in array for area and perim
    area = [0 for i in range(num)]
    perim = [0 for i in range(num)]
    for row in range(len(regions)):
        for col in range(len(regions[0])):
            # area is just 1
            area[regions[row][col]] += 1

            # perim goes up for each bordering that's diff
            crop = regions[row][col]
            if r(regions, row - 1, col) != crop:
                perim[crop] += 1
            if r(regions, row + 1, col) != crop:
                perim[crop] += 1
            if r(regions, row, col - 1) != crop:
                perim[crop] += 1
            if r(regions, row, col + 1) != crop:
                perim[crop] += 1

    # cost is the sum of the products of likewise elements
    cost = 0
    for i in range(num):
        cost += area[i] * perim[i]
    return cost

# get top cell of a region by id
def getTopCell(regions, id):
    for row in range(len(regions)):
        for col in range(len(regions[0])):
            if regions[row][col] == id:
                return row, col

# return dest coords for given spot and direction
def dest(regions, id, row, col, dir):
    match dir:
        case "E":
            return row, col + 1
        case "S":
            return row + 1, col
        case "W":
            return row, col - 1
        case "N":
            return row - 1, col

# for part 2, we need the number of sides
# this finds the number of _exterior_ sides by using a left-hand-path walk of the wall
def exteriorSides(regions, id):
    sides = 0
    startrow, startcol = getTopCell(regions, id)
    dir = "E"

    row, col = startrow, startcol

    while (row != startrow or col != startcol) or sides < 4:
        # take one step, we always want to turn left to hug the perimiter
        # we figure out our preferred directions based on that
        match dir:
            case "E":
                prefs = ["N", "E", "S", "W"]
            case "S":
                prefs = ["E", "S", "W", "N"]
            case "W":
                prefs = ["S", "W", "N", "E"]
            case "N":
                prefs = ["W", "N", "E", "S"]

        # try to turn left
        leftrow, leftcol = dest(regions, id, row, col, prefs[0])
        if r(regions, leftrow, leftcol) == id:
            row, col = leftrow, leftcol
            dir = prefs[0]
            sides += 1
            continue

        # try to go straight
        straightrow, straigthcol = dest(regions, id, row, col, prefs[1])
        if r(regions, straightrow, straigthcol) == id:
            row, col = straightrow, straigthcol
            continue

        # turn right in place
        dir = prefs[2]
        sides += 1

    # turn until we are going east again
    match dir:
        case "N":
            sides += 1
        case "E":
            sides += 0
        case "S":
            sides += 3
        case "W":
            sides += 2
    return sides

# return True if we can get to edge
def dfsToEdge(regions, id, row, col, visited):
    #print("     ", row, col)
    if row < 0 or row >= len(regions) or col < 0 or col >= len(regions[0]):
        return True
    if regions[row][col] != id:
        return False
    if visited[row][col]:
        return False

    visited[row][col] = True
    if dfsToEdge(regions, id, row - 1, col, visited):
        return True
    if dfsToEdge(regions, id, row + 1, col, visited):
        return True
    if dfsToEdge(regions, id, row, col - 1, visited):
        return True
    if dfsToEdge(regions, id, row, col + 1, visited):
        return True
    return False

def lockedIn(regions, id):
    row, col = getTopCell(regions, id)
    #print("Seeing if * region at", row, col, "is locked in ...", end=" ")
    visited = [[False for i in range(len(regions[0]))] for j in range(len(regions))]
    locked = not dfsToEdge(regions, id, row, col, visited)
    #print(locked)
    return locked


# we now need to find the overall number of sides to a region
# based on exterior AND interior ones
def numSides(regions, id, symbol):
    # step one, find the exterior sides using above function
    exteriors = exteriorSides(regions, id)

    # now we make a new grid with this one having its symbol
    # and all others being a different symbol *
    # that way we treat them all as equal and look for interior regisons
    #print("Doing it for", id, symbol)
    newgrid = [["*" for i in range(len(regions[0]))] for j in range(len(regions))]
    for row in range(len(regions)):
        for col in range(len(regions[0])):
            if regions[row][col] == id:
                newgrid[row][col] = symbol
            #print(newgrid[row][col], end="")
        #print()

    newRegions, newNum, newSymbols = findRegions(newgrid)
    interiorSides = 0
    
    # for each of these new regions, see if we can reach the border of the map or not
    # if we can't it's exteriorSides must be added to the OVERALL ones sides
    for region in range(newNum):
        # if it's the same thingy, then no
        if newSymbols[region] == symbol:
            continue

        if lockedIn(newRegions, region):
            #print("Adding in", exteriorSides(newRegions, region))
            interiorSides += exteriorSides(newRegions, region)
    
    # now we know total number of sides
    return exteriors + interiorSides

def part2(regions, num, symbols):
    # area is same, but now we get sides instead of perim
    area = [0 for i in range(num)]
    sides = [numSides(regions, i, symbols[i]) for i in range(num)]

    for row in range(len(regions)):
        for col in range(len(regions[0])):
            # area is just 1
            area[regions[row][col]] += 1

    # cost is the sum of the products of likewise elements
    cost = 0
    for i in range(num):
        print("Region", i, "has", sides[i], "sides")
        cost += area[i] * sides[i]
    return cost

sys.setrecursionlimit(20000)
grid = getInput()
regions, num, symbols = findRegions(grid)
print("There are", num, "regions")
cost = part2(regions, num, symbols)
print(cost)

