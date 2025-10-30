import heapq
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

# a simpler bfs algorithm
def pathTo(pad, start, stop, order):
    row, col = find(pad, start)
    path = ""
    endrow, endcol = find(pad, stop)
    visited = [[False for i in range(len(pad[0]))] for j in range(len(pad))]

    queue = []
    while not (row == endrow and col == endcol):
        visited[row][col] = True
        
        # we try all the orders to get best path
        for dir in order:
            if dir == "<" and get(pad, row, col - 1) != None:
                queue.append((row, col - 1, path + "<"))
            if dir == "v" and get(pad, row + 1, col) != None:
                queue.append((row + 1, col, path + "v"))
            if dir == ">" and get(pad, row, col + 1) != None:
                queue.append((row, col + 1, path + ">"))
            if dir == "^" and get(pad, row - 1, col) != None:
                queue.append((row - 1, col, path + "^"))
       
        if len(queue) == 0:
            print("No path found from", start, "to", stop)
            return None

        # take off the next thingy
        row, col, path = queue[0]
        queue = queue[1:]
    
    return path

def fullPath(pad, string, order):
    result = ""
    last = "A"
    for key in string:
        result += pathTo(pad, last, key, order)
        result += "A"
        last = key
    return result

def fullToRoom(room, order):
    level1 = fullPath(pad1, room, order)
    level2 = fullPath(pad2,  level1, order)
    level3 = fullPath(pad2,  level2, order)
    return len(level3)

def allOrders(options):
    if len(options) == 0:
        return []
    if len(options) == 1:
        return options
    orders = []
    for i in range(len(options)):
        others = allOrders(options[:i] + options[i+1:])
        for other in others:
            orders.append(options[i] + other)
    return orders


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

def part1():
    rooms = getInput()
    orders = allOrders("<>^v")
    total = 0
    for room in rooms:
        min = None
        for order in orders:
            length = fullToRoom(room, order)
            if min == None or min > length:
                min = length
        total += min * numPart(room)
    return total

print(part1())



