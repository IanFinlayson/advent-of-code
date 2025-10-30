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

def after2K(start):
    for i in range(2000):
        start = next(start)
    return start

seeds = getInput()
total = 0
for seed in seeds:
    result = after2K(seed)
    total += result

print(total)

