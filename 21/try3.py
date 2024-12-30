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
        return [""]

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


def bestPath(pad, path, level):
    if level == 0:
        return path

    start = find(pad, "A")

    total = ""
    for key in path:
        end = find(pad, key)
        #print("All paths from", pad[start[0]][start[1]], "to", pad[end[0]][end[1]], ":")
        posses = allPaths(pad1, start[0], start[1], end[0], end[1])
        #print(posses)

        #print("From", start, "to", end)
        best = None
        for poss in posses:
            # find the best one in the pad 2 at one less level
            option = bestPath(pad2, poss + "A", level - 1)
            if best == None or len(option) < len(best):
                best = option
        if best == None:
            print("rutro, could find no option for", key, "in", path)
            print(posses)
        total += best

        start = end
    return total


def numPart(room):
    firstNum = False
    number = ""
    for dig in room:
        if dig == "0" and not firstNum:
            pass
        elif dig in "0123456789":
            firstNum = True
            number = number + dig
    return int(number)


# do it for all input rooms
rooms = getInput()
part1 = 0
for room in rooms:
    t = bestPath(pad1, room, 3)
    print(t)
    print(len(t))
    part1 += numPart(room) * len(t)
print(part1)


