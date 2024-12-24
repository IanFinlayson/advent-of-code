import sys

def sortedPair(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    edges = set()
    nodes = set()
    with open(sys.argv[1]) as file:
        for line in file:
            a, b = line[:-1].split("-")
            if a not in nodes:
                nodes.add(a)
            if b not in nodes:
                nodes.add(b)
            edges.add(sortedPair(a, b))
    return edges, list(nodes)

def part1(nodes, edges):
    count = 0
    all = 0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                all += 1
                a = nodes[i]
                b = nodes[j]
                c = nodes[k]
                # check the combo
                if sortedPair(a, b) in edges and sortedPair(a, c) in edges and sortedPair(b, c) in edges:
                    if a[0] == "t" or b[0] == "t" or c[0] == "t":
                        #print(a, b, c)
                        count += 1
    return count

edges, nodes = getInput()
#print(len(nodes))
print(part1(nodes, edges))



