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

grid = getInput()
regions, num = findRegions(grid)
print("There are", num, "regions")
cost = part1(regions, num)
print(cost)


