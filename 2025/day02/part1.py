def invalid(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    return a == b


def findInvalids(start, stop):
    total = 0
    for i in range(start, stop+1):
        if invalid(i):
            total += i
    return total


def main():
    line = input().split(",")
    total = 0
    for thing in line:
        a, b = thing.split("-")
        total += findInvalids(int(a), int(b))
    print(total)


main()



