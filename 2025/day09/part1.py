def getReds():
    reds = []
    while True:
        try:
            reds.append(tuple(map(int, input().split(","))))
        except EOFError:
            return reds

def getBiggestRec(reds):
    biggest = 0

    # just try them all?
    for i in range(len(reds)):
        for j in range(i + 1, len(reds)):
            area = (1 + abs(reds[i][0] - reds[j][0])) * (1 + abs(reds[i][1] - reds[j][1]))
            if area > biggest:
                biggest = area
    return biggest

def main():
    reds = getReds()
    print(getBiggestRec(reds))


main()


