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
# we also have an AVOID node...if we hit that one we return 0
# (this way we don't count (svr->dac->fft) as a path from svr to fft
def waysToReachOut(nodes, edges, n, memo, dest, avoid):
    if memo[n] != None:
        return memo[n]

    # base case: we ARE at end
    if nodes[n] == dest:
        return 1

    # case case: we hit the avoid node
    if nodes[n] == avoid:
        return 0

    # recursive case: go through out edges
    ways = 0
    for e in edges[n]:
         ways += waysToReachOut(nodes, edges, e, memo, dest, avoid)
    memo[n] = ways
    return ways


def main():
    nodes, edges = getGraph()

    # find ways from svr to dac/fft and from dac/fft to out
    a = waysToReachOut(nodes, edges, lookup(nodes, "svr"), [None for i in range(len(nodes))], "dac", "fft")
    b = waysToReachOut(nodes, edges, lookup(nodes, "svr"), [None for i in range(len(nodes))], "fft", "dac")
    c = waysToReachOut(nodes, edges, lookup(nodes, "dac"), [None for i in range(len(nodes))], "out", "fft")
    d = waysToReachOut(nodes, edges, lookup(nodes, "fft"), [None for i in range(len(nodes))], "out", "dac")

    # ALSO dac-fft and fft-dac
    e = waysToReachOut(nodes, edges, lookup(nodes, "dac"), [None for i in range(len(nodes))], "fft", "svr")
    f = waysToReachOut(nodes, edges, lookup(nodes, "fft"), [None for i in range(len(nodes))], "dac", "svr")

    # find total paths possible
    print(a,b,c,d,e,f)
    print(a*f*d + c*e*b)



main()

