# this is just a brute force solution
# I was on vacation when this day dropped and didn't have time to
# solve this properly (or at least write it in C with parallelization)
# but I *did* have time to run it in the hotel for 15 hours LOL

import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    seeds = []
    with open(sys.argv[1]) as file:
        for line in file:
            seeds.append(int(line))
    return seeds

def next(seed):
    num = ((seed << 6)  ^ seed) & 16777215
    num = ((num >> 5) ^ num) & 16777215
    num = ((num << 11) ^ num) & 16777215
    return num

# not all sequences are possible, like we can't go up by 9, then up by 9 again like
def isPossible(seq):
    min = 0
    max = 9
    for change in seq:
        min += change
        max += change
        if min > 9 or max < 0:
            return False
    return True

def getPossibleSeqs():
    seqs = []
    for a in range(-9, 10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    seq = [a, b, c, d]
                    if isPossible(seq):
                        seqs.append(seq)
    return seqs

def getPrice(last, seq):
    history = []
  
    # prime the pump
    for i in range(4):
        n = next(last)
        history.append((n % 10) - (last % 10))
        last = n

    # now loop 1996 times (2000 minus the 4 we prepped)
    for i in range(1996):
        if history == seq:
            return last % 10
        n = next(last)
        history = history[1:] + [(n % 10) - (last % 10)]
        last = n
    
    # we never saw it, return 0
    return 0
   
# try this seq on every customer and figure out how many bananas we get
def doSeq(seeds, seq, p=False):
    bananas = 0
    for seed in seeds:
        price = getPrice(seed, seq)
        bananas += price
        if p:
            print("Price for seed", seed, "is", price)
    return bananas

# go through every possible sequence and try it
seeds = getInput()
seqs = getPossibleSeqs()

max = 0
winning_seq = 0
i = 0
for seq in seqs:
    print("Seq", i, "out of", len(seqs))
    bananas = doSeq(seeds, seq)
    if bananas > max:
        max = bananas
        winning_seq = i
    i += 1
print(max)

#print("winning seq index = ", winning_seq, ": ", end="", sep="")
#print(seqs[winning_seq])
#doSeq(seeds, seqs[winning_seq], True)



