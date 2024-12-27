import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    rooms = []
    with open(sys.argv[1]) as file:
        for line in file:
            rooms.append(line[:-1])
    return rooms

pad1 = [["7", "8", "9"],\
        ["4", "5", "6"],\
        ["1", "2", "3"],\
        [None, "0", "A"]]

pad2 = [[None, "^", "A"],\
        ["<", "v", ">"]]

def get(pad, row, col):
    if row < 0 or row >= len(pad) or col < 0 or col >= len(pad[0]):
        return None
    else:
        return pad[row][col]

# find a cell in a grid and return row, col
def find(pad, sym):
    for row in range(len(pad)):
        for col in range(len(pad[0])):
            if pad[row][col] == sym:
                return row, col
    print("Fail", sym, "not found in", pad)

# get all paths from start to stop in a pad
def allPaths(pad, r0, c0, r1, c1):
    # if we are here, no path needed
    if r0 == r1 and c0 == c1:
        return []
    
    # if we have only one dimension to go, just do that obvs
    if r0 == r1:
        if c1 > c0:
            move = ">"
        else:
            move = "<"
        return [move * abs(c1 - c0)]
    if c0 == c1:
        if r1 > r0:
            move = "v"
        else:
            move = "^"
        return [move * abs(r1 - r0)]

    # otherwise, we can try both horizontal and vertical paths
    options = []

    # horizontal first
    if c1 > c0:
        colmod = 1
        dir = ">"
    else:
        colmod = -1
        dir = "<"
    scoot = get(pad, r0, c0 + colmod)
    if scoot != None:
        conts = allPaths(pad, r0, c0 + colmod, r1, c1)
        for cont in conts:
            options.append(dir + cont)
    
    # next vertical
    if r1 > r0:
        rowmod = 1
        dir = "v"
    else:
        rowmod = -1
        dir = "^"
    scoot = get(pad, r0 + rowmod, c0)
    if scoot != None:
        conts = allPaths(pad, r0 + rowmod, c0, r1, c1)
        for cont in conts:
            options.append(dir + cont)

    return options


# try it out
start = find(pad1, "A")
end = find(pad1, "7")
paths = allPaths(pad1, start[0], start[1], end[0], end[1])
print(paths)



