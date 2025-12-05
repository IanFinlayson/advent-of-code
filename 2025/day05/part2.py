import random

class RangeSet:
    def __init__(self):
        self.ranges = []

    def sort(self):
        self.ranges.sort(key = lambda piece: piece[0])

    def countEm(self):
        count = 0
        for r in self.ranges:
            count += (r[1] - r[0]) + 1
        return count

    def simplifyOnce(self):
        for i in range(len(self.ranges)):
            for j in range(len(self.ranges)):
                if i == j:
                    continue

                a = self.ranges[i]
                b = self.ranges[j]

                # case 1: a is fully before b
                if a[1] < b[0]:
                    # do nothing, look for the next range
                    pass

                # case 2: a overlaps to the left of b
                elif a[0] < b[0] and b[0] <= a[1] and b[1] > a[1] and b[0] <= a[1]:
                    # merge them
                    a[1] = b[1]
                    del self.ranges[j]
                    return True

                # case 3: a contains b
                elif a[0] <= b[0] and a[1] >= b[1]:
                    # remove b
                    del self.ranges[j]
                    return True


                # case 4: a overlaps to the right of b
                elif b[0] < a[0] and a[0] >= b[1] and a[1] > b[1] and a[0] <= b[1]:
                    # merge them
                    a[0] = b[0]
                    del self.ranges[j]
                    return True

                # case 5: a is fully after b
                elif b[1] < a[0]:
                    # do nothing, look for the next range
                    pass
        return False

    def simplify(self):
        while self.simplifyOnce():
            pass

    def addRange(self, start, stop):
        # add it, then simplify all we can
        self.ranges.append([start, stop])
        self.simplify()

    def print(self):
        for r in self.ranges:
            print(r)

def getInput():
    ranges = []
    while True:
        line = input()
        if line == "":
            break
        else:
            ranges.append(tuple(map(int, line.split("-"))))
    return ranges

def main():
    ranges = RangeSet()

    for r in getInput():
        ranges.addRange(r[0], r[1])
    ranges.sort()
    #ranges.print()
    print(ranges.countEm())

main()

