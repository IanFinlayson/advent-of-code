import math

# good ol' union-find, an under-appreciated data structure
def emptyUF(size):
    return [i for i in range(size)]

def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    else:
        return x

def union(parents, x, y):
    parents[find(parents, x)] = find(parents, y)


# this function takes the union find and returns the part 1 answer:
# the product of the size of each disjoint set
def part1(parents):
    array = parents[:]

    print("Copied parents")

    # flatten the trees out!
    change = True
    while change:
        change = False
        for i in range(len(array)):
            if array[i] == i:
                continue
            else:
                parent = array[i]
                gparent = array[parent]
                if parent != gparent:
                    array[i] = gparent
                    change = True

    print("Flattened the trees")

    # now for each index, keep track of number in tree
    treesizes = {}
    for p in array:
        if p not in treesizes:
            treesizes[p] = 1
        else:
            treesizes[p] += 1

    # get a reverse sorted list of the values
    top3 = sorted(list(treesizes.values()), reverse=True)
    return top3[0] * top3[1] * top3[2]

def getBoxes():
    boxes = []
    while True:
        try:
            boxes.append(tuple(map(int, input().split(","))))
        except EOFError:
            return boxes

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

# returns a table [from][to] of distances
# it is "jagged" where from < to
def closestPoints(boxes):
    table = []

    for i in range(len(boxes)):
        row = []
        for j in range(i + 1, len(boxes)):
            row.append(distance(boxes[i], boxes[j]))
        table.append(row)
    return table

def main():
    # read the points and pre-compute a distances table
    boxes = getBoxes()
    print("Got the boxes")
    dist_table = closestPoints(boxes)
    print("Got the distance table")

    # we make a union/find of points to keep track of the circuits
    circuits = emptyUF(len(boxes))
    inds = len(boxes)
    print("Built the starter union/find")

    for k in range(1000):
        # go through removing smallest point, and unioning them
        mini = 0
        minj = 1
        mindist = math.inf
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                if dist_table[i][j - (i+1)] != None and dist_table[i][j - (i+1)] < mindist:
                    mini = i
                    minj = j
                    mindist = dist_table[i][j - (i+1)]

        # now we want to connect up mini and minj, and remove this distance...
        if find(circuits, mini) != find(circuits, minj):
            union(circuits, mini, minj)
            inds -= 1

        dist_table[mini][minj - (mini+1)] = None
        print("Did link", k+1, "of 1000")
    
    # do the actual thing
    print(part1(circuits))


main()

