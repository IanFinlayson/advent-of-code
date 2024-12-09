import sys
import re

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    with open(sys.argv[1]) as file:
        return file.read().rstrip()

# converts the '12345' rep to the '0..111....22222' rep
# we use a list of ints though where '.' is -1
def expand(disk):
    newdisk = []
    idx = 0
    for sym in disk:
        if idx % 2 == 0:
            newdisk += [idx // 2 for i in range(int(disk[idx]))]
        else:
            newdisk += [-1 for i in range(int(disk[idx]))]
        idx += 1
    return newdisk

def defragPart1(disk):
    l = disk.index(-1)
    r = len(disk) - 1
    while l <= r:
        disk[l], disk[r] = disk[r], disk[l]
        while disk[l] != -1:
            l += 1
        while disk[r] == -1:
            r -= 1
    return disk

def defragPart2(disk):
    # TODO...
    pass

def checksum(disk):
    cs = 0
    for blocknum in range(len(disk)):
        if disk[blocknum] != -1:
            cs += blocknum * disk[blocknum]
    return cs

print(checksum(defragPart2(expand(getInput()))))

