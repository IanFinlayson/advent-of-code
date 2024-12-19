import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    patterns = []
    designs = []
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        pattenrs = (lines[0])[:-1].split(", ")
        for line in lines[2:]:
            designs.append(line[:-1])
    return pattenrs, designs

def letterIndex(letter):
    letters = "wubrg$"
    for i in range(len(letters)):
        if letters[i] == letter:
            return i
    print("Invalid letter found in towel colors: '", letter, "'", sep="")

# we make a prefix tree for the patterns available
class Node:
    def __init__(self, sequence):
        self.sequence = sequence
        self.leaf = True
        self.children = None

    def contains(self, searchSequence, i=0):
        if self.leaf:
            return self.sequence == searchSequence
        else:
            letter = searchSequence[i] if i < len(searchSequence) else "$"
            child = self.children[letterIndex(letter)]
            if child == None:
                return False
            else:
                return child.contains(searchSequence, i + 1)

    def makeInterior(self):
        self.leaf = False
        self.sequence = None
        self.children = [None for i in range(6)]  # we store 5 for the actual colors + 1 for end($)

    def print(self, indents=0):
        lead = "  " * indents

        if self.leaf:
            print(lead + self.sequence)
        else:
            print(lead + "I")
            for child in self.children:
                if child == None:
                    print(lead + "E")
                else:
                    child.print(indents + 1)

    def insert(self, newSequence, i=0):
        # if this is a leaf, we must split it
        if self.leaf:
            # get the old sequence out, which needs to be inserted
            oldSequence = self.sequence
            if oldSequence == newSequence:
                print("Oh no duplicate inserted???")
                return

            # make interior, then recursively insert both things
            self.makeInterior()
            self.insert(oldSequence, i)
            self.insert(newSequence, i)
        else:
            # this is an interior way-finding node
            letter = newSequence[i] if i < len(newSequence) else "$"
            child = self.children[letterIndex(letter)]

            if child == None:
                # if nothing here, make a new leaft
                self.children[letterIndex(letter)] = Node(newSequence)
            else:
                # send it down the chain
                child.insert(newSequence, i + 1)

# TODO memoize this thing


# returns if a given design can be made given available patterns (prefix tree)
def numPossible(tree, design):
    # base case, if design empty, it works
    if design == "":
        return 1

    count = 0
    for length in range(1, len(design) + 1):
        part1 = design[:length]
        part2 = design[length:]

        # if part1 is in tree, and rest works, we're good
        if tree.contains(part1):
            count += numPossible(tree, part2)

    return count

def part2(tree, designs):
    count = 0
    for design in designs:
        print(design, "...", end="")
        count += numPossible(root, design)
        print(count)
    return count

# get the initial inputs
patterns, designs = getInput()

# build up the tree
root = Node(patterns[0])
for pat in patterns[1:]:
    root.insert(pat)

print(part2(root, designs))



