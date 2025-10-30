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
def dijkstra(graph, source, dest):
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
                distance = tentative[index] + 1

                if tentative[other] == None or distance < tentative[other]:
                    tentative[other] = distance
                    path[other] = path[index] + graph[index][other]
                    heapq.heappush(nodes, (distance, other))

    return path[dest]

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

def applyDijkstra(graph, indexFunc, sequence):
    result = ""
    last = indexFunc("A")
    for key in sequence:
        path = dijkstra(graph, last, indexFunc(key))
        result += path + "A"
        last = indexFunc(key)
    return result


def part1(numeric, directional, room):
    #print(room, ": ", sep="", end="")
    print(room)

    level1 = applyDijkstra(numeric, roomToIndex, room)
    level2 = applyDijkstra(directional, dirToIndex, level1)
    level3 = applyDijkstra(directional, dirToIndex, level2)

    print(level1)
    print(level2)
    print(level3)
    print(len(level3))
    return len(level3) * int(room[:-1])


numeric = numericGraph()
directional = directionalGraph()

#total = 0
#for room in getInput():
#    total += part1(numeric, directional, room)
#print(total)
    

part1(numeric, directional, "456A")
print("\nCorrect:\n456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A")


