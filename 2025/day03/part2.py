def asnum(s):
    if s == "":
        return 0
    else:
        return int(s)

memo = dict()

# we return the max possible jolts in the bank starting at i, with remaining batteries left
def maxJoltage(bank, i, remaining):
    # return pre-computed if memoized
    if str((i, remaining)) in memo:
        return memo[str((i, remaining))]

    if i == len(bank):
        return ""
    if remaining == 0:
        return ""

    # we include this one, or we dont
    include = bank[i] + maxJoltage(bank, i + 1, remaining - 1)
    dont = maxJoltage(bank, i + 1, remaining)

    # return the better option
    if asnum(include) > asnum(dont):
        answer = include
    else:
        answer = dont
    memo[str((i, remaining))] = answer
    return answer

def process(bank):
    memo.clear()
    jolts = maxJoltage(bank, 0, 12)
    return int(jolts)

def main():
    total = 0
    while True:
        try:
            bank = input()
            total += process(bank)
        except EOFError:
            break
    print(total)

main()


