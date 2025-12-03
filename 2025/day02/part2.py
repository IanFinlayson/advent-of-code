def invalid1(num, amt):
    s = str(num)
    if len(s) % amt != 0:
        return False
    stride = len(s)//amt
    prev = s[:stride]
    for i in range(1, amt):
        nextp = s[stride*i:stride*(i+1)]
        if prev != nextp:
            return False
    return True
    

def invalid(num):
    # I just put 10 as the max number of repeats and it worked
    # ideally we would find the max possible based on the number size
    for i in range(2, 10):
        if invalid1(num, i):
            return True
    return False

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



