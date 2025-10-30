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

def getTries(nodes, edges):
    count = 0
    tries = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                a = nodes[i]
                b = nodes[j]
                c = nodes[k]
                # check the combo
                if sortedPair(a, b) in edges and sortedPair(a, c) in edges and sortedPair(b, c) in edges:
                    tries.append(set([a, b, c]))
    return tries

# try and expand cliques by checking for nodes which can be added in
def expandCliques(cliques, nodes, edges):
    expandeds = []
    for clique in cliques:
        for node in nodes:
            if node in clique:
                continue
            addit = True
            for piece in clique:
                if sortedPair(piece, node) not in edges:
                    addit = False
            if addit:
                thing = clique.union([node])
                if thing not in expandeds:
                    expandeds.append(clique.union([node]))
    return expandeds

# expand the sets of three from part 1 until there is one biggest clique
def biggestClique(cliques, nodes, edges):
    while len(cliques) > 1:
        print("Got cliques down to", len(cliques))
        cliques = expandCliques(cliques, nodes, edges)
    return cliques

edges, nodes = getInput()
tries = getTries(nodes, edges)
biggest = biggestClique(tries, nodes, edges)

answer = sorted(list(biggest))
for thing in answer[:-1]:
    print(thing,end=",")
print(answer[-1])

