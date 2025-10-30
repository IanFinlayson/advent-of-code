import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    grid = []
    with open(sys.argv[1]) as file:
        cases = []
        for line in file:
            things = line.split()
            winning = []
            mine = []
            seenbar = False
            for thing in things[2:]:
                if thing == "|":
                    seenbar = True
                elif seenbar:
                    mine.append(int(thing))
                else:
                    winning.append(int(thing))
            cases.append((winning, mine))
    return cases

# return the number of wins for a card
def getWins(card):
    lucky, ours = card
    wins = 0
    for num in ours:
        if num in lucky:
            wins += 1
    return wins

# given the card and its number, return the card numbers we win
def getNext(num, card):
    wins = getWins(card)
    next = []
    for i in range(wins):
        next.append(num + i + 1)
    return next

def main():
    cards = getInput()

    # loop from the last card back to the first, saving how many we get
    grandtotal = 0
    winnings = {}
    for cardnum in range(len(cards), 0, -1):
        nexts = getNext(cardnum, cards[cardnum - 1])
        total = 0
        for n in nexts:
            total += winnings[n]
        winnings[cardnum] = 1 + total
        grandtotal += 1 + total

    print(grandtotal)

main()

