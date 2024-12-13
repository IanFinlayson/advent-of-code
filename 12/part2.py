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

# make a list of polygons from the input grid
def getPolys(grid):
    polys = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            x = col
            y = len(grid) - row
            a = (x, y + 1)
            b = (x + 1, y + 1)
            c = (x + 1, y)
            d = (x, y)
            polys.append([grid[row][col], [(a, b), (c, b), (d, c), (d, a)]])
    return polys

# loop through polys and find 2 that can be merged
# return false if none
def merge2(polys):
    a = None
    b = None
    shared = None
    found = False
    for i in range(len(polys)):
        if found:
            break
        for j in range(i + 1, len(polys)):
            if found:
                break
            if polys[i][0] == polys[j][0]:
                for edge in polys[i][1]:
                    if edge in polys[j][1]:
                        a = polys[i]
                        b = polys[j]
                        shared = edge
                        found = True
    if found:
        a[1].remove(shared)
        b[1].remove(shared)
        newedges = a[1] + b[1]
        new = [a[0], newedges]
        polys.remove(a)
        polys.remove(b)
        polys.append(new)
        return True
    else:
        return False


grid = getInput()
polys = getPolys(grid)
print("Before merge")
for poly in polys:
    print(poly)

while merge2(polys):
    pass

print("After merge")
for poly in polys:
    print(poly[0], len(poly[1]))
    for e in poly[1]:
        print("    ", e)



