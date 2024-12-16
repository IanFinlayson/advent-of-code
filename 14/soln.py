import sys

# I reformatted the input in vim to avoid parsing
def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    bots = []
    l = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if l == 0:
                cols = int(line)
            elif l == 1:
                rows = int(line)
            else:
                bots.append(list(map(int, line.split())))
            l += 1
    return rows, cols, bots

# return new col,row for a bot
def stepbot(col, row, dcol, drow, rows, cols):
    c = col + dcol
    while c >= cols:
        c -= cols
    while c < 0:
        c += cols

    r = row + drow
    while r >= rows:
        r -= rows
    while r < 0:
        r += rows
    return c, r

def step(bots, rows, cols):
    for b in range(len(bots)):
        c, r = stepbot(bots[b][0], bots[b][1], bots[b][2], bots[b][3], rows, cols)
        bots[b][0] = c
        bots[b][1] = r

def botGrid(bots, rows, cols):
    counts = [[0 for i in range(cols)] for j in range(rows)]

    for b in bots:
        c = b[0]
        r = b[1]
        counts[r][c] += 1
    return counts

def p(counts):
    for row in counts:
        for thing in row:
            if thing == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()

def part1Score(counts):
    nw = 0
    ne = 0
    sw = 0
    se = 0
    rows = len(counts)
    cols = len(counts[0])


    for row in range(rows):
        north = False
        south = False
        if row < ((rows / 2) - 1):
            north = True
        elif row > (rows / 2):
            south = True

        for col in range(cols):
            east = False
            west = False
            if col < ((cols / 2) - 1):
                west = True
            elif col > (cols / 2):
                east = True

            # add this one
            if north and west:
                nw += counts[row][col]
            if north and east:
                ne += counts[row][col]
            if south and west:
                sw += counts[row][col]
            if south and east:
                se += counts[row][col]
    return nw * ne * sw * se

# we just look for so many bots in a row, which the xmas tree has
# this one was kinda poorly specified, so I saw a picture in the discord before I understood what it meant
def hasTree(counts):
    poss = False
    for row in range(rows):
        seq = 0
        for col in range(cols):
            if counts[row][col] > 0:
                seq += 1
            else:
                seq = 0

            if seq > 8:
                poss = True
    return poss

rows, cols, bots = getInput()

# find the xmas tree
for i in range(10000):
    counts = botGrid(bots, rows, cols)
    step(bots, rows, cols)
    if hasTree(counts):
        print(i)
        p(counts)

