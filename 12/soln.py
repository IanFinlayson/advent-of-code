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

    nextrow, nextcol = 0, 0
    nextid = 0
    done = False

    while not done:
        # flood fill nextrow, nextcol
        floodID(grid[nextrow][nextcol], grid, regions, nextrow, nextcol, nextid)

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
    return regions, nextid + 1

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
# to do this, we find the top/left most cell and walk the perimiter until we get back
def numSides(regions, id):
    sides = 0
    startrow, startcol = getTopCell(regions, id)
    dir = "E"

    row, col = startrow, startcol

    while (row != startrow or col != startcol) or sides < 4:
        #print("(", row, ", ", col, ") ", dir, sep="")
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
            #print("Left turn")
            row, col = leftrow, leftcol
            dir = prefs[0]
            sides += 1
            continue

        # try to go straight
        straightrow, straigthcol = dest(regions, id, row, col, prefs[1])
        if r(regions, straightrow, straigthcol) == id:
            #print("Straight")
            row, col = straightrow, straigthcol
            continue

        # turn right in place
        #print("Right turn")
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

def part2(regions, num):
    # area is same, but now we get sides instead of perim
    area = [0 for i in range(num)]
    sides = [numSides(regions, i) for i in range(num)]

    # TODO we need to adjust this for regions entirely inside of others
    # those interior ones need their side counts added to the enclosing one ...

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


grid = getInput()
regions, num = findRegions(grid)
print("There are", num, "regions")
cost = part2(regions, num)
print(cost)



