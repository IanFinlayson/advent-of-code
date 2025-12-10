def getInput():
    line = input().split()
    end_config = [ c == '#' for c in reversed(line[0][1:-1])]
    jolts = list(map(int, line[-1][1:-1].split(",")))
    switches = []
    for s in line[1:-1]:
        switches.append(list(map(int, s[1:-1].split(","))))
    return end_config, switches, jolts

def asBinary(end_config):
    number = 0
    pos = 1
    for bit in reversed(end_config):
        if bit:
            number += pos
        pos <<= 1
    return number

def nextConfig(node, switch):
    config = node

    # each thingy that gets flipped for this switch is straight up a bit position
    for flip in switch:
        mask = 1 << flip
        config ^= mask
    return config

def buildGraph(size, switches):
    # we build a graph with 2^size nodes, which each represent a state of the switches
    # (this is OK because the largest input is 10 giving us 1024 nodes)
    # an edge is present from one state to another if there is a switch which gets us there

    # the graph is an adjacency matrix of booleans
    matrix = [[False for i in range(2 ** size)] for j in range(2 ** size)]

    # for each possible switch configuration state
    for node in range(2 ** size):
        # for each switch we can pull in this state
        for switch in switches:
            # find what state this switch would take us to
            next = nextConfig(node, switch)

            # insert this connection into the matrix
            matrix[node][next] = True
    return matrix

# now that we have a graph, we can simply shortest-path search
# from the 0 state (all switches off) to the desired state
# because the graph is unweighted, this is a simple BFS
def shortestPath(matrix, start_config, end_config):
    queue = []
    visited = [False for i in range(len(matrix))]

    steps = 0
    current = start_config
    while current != end_config:
        visited[current] = True

        # for each other state
        for potential in range(len(matrix)):
            # if we can go there and it's not been visited, append it
            if matrix[current][potential] and not visited[potential]:
                queue.append((potential, steps + 1))

        # if the queue is empty, we're done
        if len(queue) == 0:
            print("No path to the desired state!")
            return -1

        # get the next state from the queue
        current, steps = queue.pop(0)
    return steps

def main():
    total = 0

    # do this for all of them until EOF
    while True:
        try:
            end_config, switches, jolts = getInput()
            matrix = buildGraph(len(end_config), switches)
            total += shortestPath(matrix, 0, asBinary(end_config))
        except EOFError:
            break
    print(total)

main()

