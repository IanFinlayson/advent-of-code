import sys
import math

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

def find_stations(grid):
    stations = dict()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                if grid[row][col] in stations:
                    stations[grid[row][col]].append((row, col))
                else:
                    stations[grid[row][col]] = ([(row, col)])
    return stations

def antiNodesPart1(n1, n2, rows, cols, anodes):
    # just realized x and y are mixed up, but whatevs
    xdiff = n1[0] - n2[0]
    ydiff = n1[1] - n2[1]

    potential1 = (n1[0] + xdiff, n1[1] + ydiff)
    potential2 = (n2[0] - xdiff, n2[1] - ydiff)

    if potential1[0] >= 0 and potential1[0] < rows and potential1[1] >= 0 and potential1[1] < cols:
        anodes[potential1[0]][potential1[1]] = True
    if potential2[0] >= 0 and potential2[0] < rows and potential2[1] >= 0 and potential2[1] < cols:
        anodes[potential2[0]][potential2[1]] = True

def antiNodesPart2(n1, n2, rows, cols, anodes):
    # just realized x and y are mixed up, but whatevs
    xdiff = n2[0] - n1[0]
    ydiff = n2[1] - n1[1]

    # simplify the fraction
    xdiff //= math.gcd(xdiff, ydiff)
    ydiff //= math.gcd(xdiff, ydiff)

    # scan in one direction
    oob = False
    lastx = n1[0]
    lasty = n1[1]
    while not oob:
        nx = lastx + xdiff
        ny = lasty + ydiff
        if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
            anodes[nx][ny] = True
            lastx = nx
            lasty = ny
        else:
            oob = True

    # scan in the other
    oob = False
    lastx = n2[0]
    lasty = n2[1]
    while not oob:
        nx = lastx - xdiff
        ny = lasty - ydiff
        if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
            anodes[nx][ny] = True
            lastx = nx
            lasty = ny
        else:
            oob = True


# return number of anti-nodes
def part1(stations, rows, cols, anodes):
    for (station, locs) in stations.items():
        # we need to pick every pair of locations
        for first in range(len(locs)):
            for second in range(first + 1, len(locs)):
                antiNodesPart2(locs[first], locs[second], rows, cols, anodes)

def countEm(anodes):
    count = 0
    for row in anodes:
        for thing in row:
            if thing:
                count += 1
    return count

grid = getInput()
stations = find_stations(grid)
antinodes = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
part1(stations, len(grid), len(grid[0]), antinodes)
print(countEm(antinodes))


