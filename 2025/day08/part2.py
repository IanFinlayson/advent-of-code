import math
import heapq

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

def getBoxes():
    boxes = []
    while True:
        try:
            boxes.append(tuple(map(int, input().split(","))))
        except EOFError:
            return boxes

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

# returns a min heap of the distances
# the array is (dist, (p1, p2))
def closestPoints(boxes):
    minheap = []

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            heapq.heappush(minheap, (distance(boxes[i], boxes[j]), i, j))
    return minheap

def main():
    # read the points and pre-compute a distances table
    boxes = getBoxes()
    print("Got the boxes")
    minheap = closestPoints(boxes)
    print("Got the distance table")

    # we make a union/find of points to keep track of the circuits
    circuits = emptyUF(len(boxes))
    inds = len(boxes)
    print("Built the starter union/find")

    while inds > 1:
        (mindist, mini, minj) = heapq.heappop(minheap)

        # now we want to connect up mini and minj, and remove this distance...
        if find(circuits, mini) != find(circuits, minj):
            union(circuits, mini, minj)
            inds -= 1

    # we have now connected up all of the boxes!!
    print("Done")
    print(boxes[mini][0] * boxes[minj][0])
    

main()

