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

def getQuads(edges, nodes):
    # we can compute these, but to not re-do it, we cache it instead
    
    # COMPUTE QUADS
    # tries = getTries(nodes, edges)
    # quads = expandCliques(tries, nodes, edges)
    
    # GET QUADS FROM CACHE
    with open("quads.txt") as quadfile:
        line = quadfile.readline()
        quads = eval(line)
    return quads




edges, nodes = getInput()

quads = getQuads(edges, nodes)

#quines = expandCliques(quads, nodes, edges)
with open("quines.txt") as infile:
    line = infile.readline()
    quines = eval(line)

#sextups = expandCliques(quines, nodes, edges)
with open("sextups.txt") as infile:
    line = infile.readline()
    sextups = eval(line)

#sevs = expandCliques(sextups, nodes, edges)
with open("sevs.txt") as infile:
    line = infile.readline()
    sevs = eval(line)



#ochos = expandCliques(sevs, nodes, edges)
#print(ochos)
with open("ochos.txt") as infile:
    line = infile.readline()
    ochos = eval(line)

#niners = expandCliques(ochos, nodes, edges)
#tens = expandCliques(niners, nodes, edges)
#onces = expandCliques(tens, nodes, edges)
with open("onces.txt") as infile:
    line = infile.readline()
    onces = eval(line)

#twelves = expandCliques(onces, nodes, edges)
with open("twelves.txt") as infile:
    line = infile.readline()
    twelves = eval(line)

#thirteens = expandCliques(twelves, nodes, edges)
# GOT IT!
with open("thirteens.txt") as infile:
    line = infile.readline()
    thirteens = eval(line)
    

answer = list(thirteens[0])
for thing in sorted(answer):
    print(thing,end=",")
print()

