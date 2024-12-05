import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    rules = []
    updates = []
    dest = rules
    delim = "|"
    with open(sys.argv[1]) as file:
        for line in file:
            if line == "\n":
                # read into updates now
                dest = updates
                delim = ","
            else:
                dest.append(list(map(int, line[:-1].split(delim))))
    return rules, updates


def isValid(rules, update):
    # check each rule is valid
    for rule in rules:
        # if either not in update, carry on
        if rule[0] not in update or rule[1] not in update:
            continue
        # ensure right one comes first
        aloc = update.index(rule[0])
        bloc = update.index(rule[1])
        if aloc > bloc:
            return False
    return True

def middle(update):
    mid = len(update) // 2
    return update[mid]

def part1(rules, updates):
    total = 0
    for update in updates:
        if isValid(rules, update):
            total += middle(update)
    return total

rules, updates = getInput()
print(part1(rules, updates))

