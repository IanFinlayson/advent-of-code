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

# this uses a top-sort like algorithm
def fix(rules, update):
    new = []

    # go until all pages scheduled
    while len(update) > 0:
        # find a page that can be scheduled
        todo = -1
        for page in update:
            possible = True
            for rule in rules:
                if page == rule[1] and rule[0] in update:
                    possible = False
            if possible:
                todo = page
                break

        # schedule this page, and remove from order
        new.append(todo)
        update.remove(todo)
    return new


def part2(rules, updates):
    total = 0
    for update in updates:
        if not isValid(rules, update):
            total += middle(fix(rules, update))
    return total

rules, updates = getInput()
print(part2(rules, updates))

