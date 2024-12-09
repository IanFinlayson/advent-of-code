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
    return newdisk, idx

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

def printdisk(disk):
    s = ""
    for num in disk:
        if num == -1:
            s += "."
        else:
            s+= str(num)
    print(s)

# this function moves one file to the right, or doesn't if it doesn't fit
# it takes the length of the disk array as a param (we subtract so to exclude considered files)
def defragPart2Step(disk, length):
    # get right indices
    r = length - 1
    while disk[r] == -1:
        r -= 1
    val = disk[r]
    rsize = 0
    while disk[r - rsize] == val:
        rsize += 1
    r -= (rsize - 1)

    #print("Attempt to move file", val, "at", r, "of size", rsize)

    offset = 0
    while True:
        try:
            # get left side
            l = disk.index(-1, offset)
            lsize = 0
            while disk[l + lsize] == -1:
                lsize += 1

            if l >= r:
                #print("Giving up :(")
                return r

            #print("Considering gap at", l, " of size", lsize, end="...")

            # if there's room here, make the switch
            if lsize >= rsize:
                #print("Match!")
                for i in range(rsize):
                    disk[l + i] = disk[r + i]
                    disk[r + i] = -1
                return r
            else:
                #print("no match.")
                # find the next gap
                offset = l + lsize
        except:
            # there was no room for this file :(
            #print("Giving up :(")
            return r

# could be more efficient than maing all these passes
def defragPart2(disk, nf):
    l = len(disk)
    #printdisk(disk)

    for i in range(nf):
        l = defragPart2Step(disk, l)
        #printdisk(disk)
        #print()

    return disk


def checksum(disk):
    cs = 0
    for blocknum in range(len(disk)):
        if disk[blocknum] != -1:
            cs += blocknum * disk[blocknum]
    return cs

disk, nf = expand(getInput())
print(nf)
disk = defragPart2(disk, nf)
print(checksum(disk))


