import sys

def getInput():
    if len(sys.argv) < 2:
        print("Please pass file name")
        sys.exit(1)
    reports = []
    with open(sys.argv[1]) as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

# part 1
def safePart1(report):
    inc = report[0] < report[1]
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff < 0 and inc:
            return False
        if diff > 0 and not inc:
            return False
    return True

# part 2
def safePart2(report):
    # if it's safe already, then yeah
    if safePart1(report):
        return True

    # otherwise try taking each thingy out first
    # this could be done more efficiently by seeing where it fails and only taking out the two on either side...
    for i in range(len(report)):
        new = report[:i] + report[i + 1:]
        if safePart1(new):
            return True
    return False

reports = getInput()
count = 0
for report in reports:
    if safePart2(report):
        count += 1
print(count)

