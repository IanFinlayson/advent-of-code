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

# returns an adjacency matrix representing the numeric keypad
# the indices are 0-9 and a is 10 (so we use hex)
# the values are the diretion to go in < > ^ v
def numericGraph():
    graph = [[None for i in range(11)] for j in range(11)]
    graph[0x0][0xA] = ">"
    graph[0x0][0x2] = "^"
    graph[0x1][0x4] = "^"
    graph[0x1][0x2] = ">"
    graph[0x2][0x1] = "<"
    graph[0x2][0x5] = "^"
    graph[0x2][0x3] = ">"
    graph[0x2][0x0] = "v"
    graph[0x3][0x2] = "<"
    graph[0x3][0x6] = "^"
    graph[0x3][0xA] = "v"
    graph[0x4][0x7] = "^"
    graph[0x4][0x5] = ">"
    graph[0x4][0x1] = "v"
    graph[0x5][0x4] = "<"
    graph[0x5][0x8] = "^"
    graph[0x5][0x6] = ">"
    graph[0x5][0x2] = "v"
    graph[0x6][0x3] = "v"
    graph[0x6][0x5] = "<"
    graph[0x6][0x9] = "^"
    graph[0x7][0x4] = "v"
    graph[0x7][0x8] = ">"
    graph[0x8][0x5] = "v"
    graph[0x8][0x7] = "<"
    graph[0x8][0x9] = ">"
    graph[0x9][0x8] = "<"
    graph[0x9][0x6] = "v"
    graph[0xA][0x0] = "<"
    graph[0xA][0x3] = "^"
    return graph

# this returns an adjacency matrix representing the directional keypad
# the indices are: > ^ < v A
#                  0 1 2 3 4
def directionalGraph():
    d = dict()
    d[">"] = 0
    d["^"] = 1
    d["<"] = 2
    d["v"] = 3
    d["A"] = 4
    graph = [[None for i in range(5)] for j in range(5)]
    graph[d[">"]][d["A"]] = "^"
    graph[d[">"]][d["v"]] = "<"
    graph[d["^"]][d["A"]] = ">"
    graph[d["^"]][d["v"]] = "v"
    graph[d["<"]][d["v"]] = ">"
    graph[d["v"]][d["<"]] = "<"
    graph[d["v"]][d["^"]] = "^"
    graph[d["v"]][d[">"]] = ">"
    graph[d["A"]][d["^"]] = "<"
    graph[d["A"]][d[">"]] = "v"
    return graph

# yet ANOTHER time dijkstra's is coming in handy this year
def dijkstra(graph, source, dest, directional, depth):
    tentative = [None for i in range(len(graph))]
    tentative[source] = 0

    path = [None for i in range(len(graph))]
    path[source] = ""

    # we make a heap of (cost, index) to explore from
    nodes = []
    heapq.heappush(nodes, (0, source))

    while len(nodes) > 0:
        tent, index = heapq.heappop(nodes)

        # try to go each place
        for other in range(len(graph)):
            if graph[index][other] != None:
                # here we can't just use 1 as a cost, but the cost to get here in the directional graph!!!!
                if depth > 0:
                    costy, ignore = dijkstra(directional, dirToIndex("A"), dirToIndex(graph[index][other]), directional, depth - 1)
                else:
                    costy = 1
                distance = tentative[index] + costy

                if tentative[other] == None or distance < tentative[other]:
                    tentative[other] = distance
                    path[other] = path[index] + graph[index][other]
                    heapq.heappush(nodes, (distance, other))

    # this is a TOTAL hack :(
    #if path[dest] == "^^<<":
    #    path[dest] = "<<^^"
    
    #if path[dest] == "^<<":
    #    path[dest] = "<<^"
    #if path[dest] == "^^^<":
    #    path[dest] = "<^^^"
    #if path[dest] == "^<":
    #    path[dest] = "<^"
    
    # return the paths in which are now a least cost path to each node
    if depth == 2:
        print("To get from", source, "to", dest, "we can do", path[dest])

    return tentative[dest], path[dest]

def roomToIndex(key):
    if key == "A":
        return 0xA
    else:
        return ord(key) - ord("0")

def dirToIndex(dir):
    d = dict()
    d[">"] = 0
    d["^"] = 1
    d["<"] = 2
    d["v"] = 3
    d["A"] = 4
    return d[dir]

def part1(numeric, directional, room):
    #print(room, ": ", sep="", end="")
    #print(room)

    level1 = ""
    last = roomToIndex("A")
    for key in room:
        cost, path = dijkstra(numeric, last, roomToIndex(key), directional, 2)
        level1 += path + "A"
        last = roomToIndex(key)
    #print(level1)

    level2 = ""
    last = dirToIndex("A")
    for d in level1:
        cost, path = dijkstra(directional, last, dirToIndex(d), directional, 1)
        level2 += path + "A"
        last = dirToIndex(d)
    #print(level2)

    level3 = ""
    last = dirToIndex("A")
    for d in level2:
        cost, path = dijkstra(directional, last, dirToIndex(d), directional, 0)
        level3 += path + "A"
        last = dirToIndex(d)
    print(level3)
    
    print(len(level3))

    return len(level3) * int(room[:-1])


numeric = numericGraph()
directional = directionalGraph()
total = 0
for room in getInput():
    total += part1(numeric, directional, room)
print(total)
    

#part1(numeric, directional, "456A")
#print("\nCorrect:\n456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A")


