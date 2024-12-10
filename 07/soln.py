import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    probs = []
    with open(sys.argv[1]) as file:
        for line in file:
            parts = line.split(": ")
            result = int(parts[0])
            nums = list(map(int, parts[1].split()))
            probs.append((result, nums))
    return probs

# evaluate given list of nums and list of operators
def evaluate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += nums[i + 1]
        elif ops[i] == "*":
            result *= nums[i + 1]
        else:
            result = int(str(result) + str(nums[i + 1]))
    return result

# takes a list of + and * and returns the next one it does this basically
# by treating + as 0 and * as 1 and adding 1 to get the next binary number
# returns whether their is no next permutation of these
def next_perm(ops):
    idx = len(ops) - 1
    while True:
        if idx < 0:
            return False
        if ops[idx] == "*":
            ops[idx] = "||"
            return True
        elif ops[idx] == "+":
            ops[idx] = "*"
            return True
        else:
            ops[idx] = "+"
            idx -= 1


# the longest line of input only has 12 numbers, so brute force activated
def resultOrZero(result, nums):
    # make a list of the ops we will need, start with plusses
    ops = ["+" for i in range(len(nums) - 1)]

    # try each possible list
    done = False
    while not done:
        if evaluate(nums, ops) == result:
            return result
        done = not next_perm(ops)
    return 0

# do the part 1 on each problem
probs = getInput()
count = 0
num = 1
for prob in probs:
    count += resultOrZero(prob[0], prob[1])
    print("Done problem", num)
    num += 1
print(count)


