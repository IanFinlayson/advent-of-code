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
        
# return all paths from given node to ending node
def waysToReachOut(nodes, edges, n, memo, dest):
    if memo[n] != None:
        return memo[n]

    # base case: we ARE at end
    if nodes[n] == dest:
        return [[n]]

    # recursive case: go through out edges
    ways = []
    for e in edges[n]:
         pathsFromHere = waysToReachOut(nodes, edges, e, memo, dest)
         for p in pathsFromHere:
             ways.append([n] + p)
    memo[n] = ways
    return ways


def main():
    nodes, edges = getGraph()

    # find ways from svr to dac, and from svr to fft
    toDAC = waysToReachOut(nodes, edges, lookup(nodes, "svr"), [None for i in range(len(nodes))], "dac")
    print("There are", len(toDAC), "ways to DAC")
    toFFT = waysToReachOut(nodes, edges, lookup(nodes, "svr"), [None for i in range(len(nodes))], "fft")
    print("There are", len(toFFT), "ways to FFT")


main()

