# looks up a node number by name, maybe optimize with a dict if needed
def lookup(nodes, name):
    for i in range(len(nodes)):
        if nodes[i] == name:
            return i

# read the input and return as a graph
# the graph contains a list of nodes where index is node number and value is label,
# and a a list of edges
def getGraph():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    nodes = []
    for line in lines:
        nodes.append(line.split()[0][:-1])
    nodes.append("out")

    edges = []
    for line in lines:
        links = line.split()[1:]
        thisun = []
        for link in links:
            thisun.append(lookup(nodes, link))
        edges.append(thisun)
    # out has none
    edges.append([])

    return nodes, edges
        
# return NUMBER of paths from given node to ending node
def waysToReachOut(nodes, edges, n, memo, dest, seenDAC, seenFFT):
    # check memo array
    if str((n, seenDAC, seenFFT)) in memo:
        return memo[str((n, seenDAC, seenFFT))]

    # base case: we ARE at end
    if nodes[n] == dest:
        return 1 if (seenDAC and seenFFT) else 0

    # check if we are a special one
    if nodes[n] == "dac":
        seenDAC = True
    if nodes[n] == "fft":
        seenFFT = True

    # recursive case: go through out edges
    ways = 0
    for e in edges[n]:
        ways += waysToReachOut(nodes, edges, e, memo, dest, seenDAC, seenFFT)
    memo[str((n, seenFFT, seenDAC))] = ways
    return ways

def main():
    nodes, edges = getGraph()
    ways = waysToReachOut(nodes, edges, lookup(nodes, "svr"), {}, "out", False, False)
    print(ways)

main()

