import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)

    list1 = []
    list2 = []
    with open(sys.argv[1]) as file:
        for line in file:
            nums = line.split()
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    return list1, list2

# part 1
def findDistance(list1, list2):
    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])
    return total

# part 2
def similarity(list1, list2):
    # to avoid going through list2 so many times, we make a hash map of
    # all the counts for each nuber in it, mapping the number to its count
    counts = {}
    for num in list2:
        if counts.get(num) == None:
            counts[num] = 1
        else:
            counts[num] = counts[num] + 1

    # now go through list1 doing the times-y thing
    diff = 0
    for num in list1:
        if counts.get(num) != None:
            diff += num * counts[num]
    return diff

list1, list2 = getInput()
print(findDistance(sorted(list1), sorted(list2)))
print(similarity(list1,list2))

