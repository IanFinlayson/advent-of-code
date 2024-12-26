import sys

# read either a lock or key, return True if lock
def getThing(file):
    thing = []
    for i in range(7):
        line = file.readline()[:-1]
        if len(line) < 1:
            return None, None
        thing.append([let for let in line])
    file.readline()
    if thing[0][0] == "#":
        return thing, True
    else:
        return thing, False

# read all the keys and locks as just grids of chars
def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    locks = []
    keys = []
    with open(sys.argv[1]) as file:
        while True:
            thing, isLock = getThing(file)
            if thing == None:
                break
            elif isLock:
                locks.append(thing)
            else:
                keys.append(thing)
    return keys, locks

def gridToHeights(thing, c):
    heights = []
    for col in range(len(thing[0])):
        height = 0
        for row in range(len(thing)):
            if thing[row][col] == c:
                height += 1
        heights.append(height)
    return heights

def getLocksAndKeys():
    keygrids, lockgrids = getInput()

    keys = []
    for keygrid in keygrids:
        keys.append(gridToHeights(keygrid, "#"))
    locks = []
    for lockgrid in lockgrids:
        locks.append(gridToHeights(lockgrid, "."))
    return locks, keys

# check if a given key and lock fit or not
def fits(lock, key):
    for pin in range(5):
        if lock[pin] < key[pin]:
            return False
    return True


def part1(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                count += 1
    return count

locks, keys = getLocksAndKeys()
print(part1(locks, keys))


