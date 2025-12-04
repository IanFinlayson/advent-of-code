import random

def getRaces():
    time = ""
    dist = ""
    times = list(map(int, input().split()[1:]))
    dists = list(map(int, input().split()[1:]))
    for i in range(len(times)):
        time += str(times[i])
        dist += str(dists[i])
    return [(int(time), int(dist))]

def wins(time, dist, amount):
    speed = amount
    travelled = (time - amount) * speed
    return travelled > dist


def waysToWin(time, dist):
    # we randomly sample the range until we find a winning point
    winningPoint = random.randint(0, time)
    while not wins(time, dist, winningPoint):
        winningPoint = random.randint(0, time)
    print(winningPoint, "is a winning point!")

    # we now binary search from 0 to here to find the minimum one that wins
    min = 0
    max = winningPoint
    while True:
        guess = (max + min) // 2
        if wins(time, dist, guess) and not wins (time, dist, guess - 1):
            # we found it!!!
            startPoint = guess
            print("Found the starting point:", startPoint)
            break
        elif wins(time, dist, guess):
            max = guess - 1
        else:
            min = guess + 1

    # we now binary search from winningPoint to end to find the MAX one that wins
    min = winningPoint
    max = time
    while True:
        guess = (max + min) // 2
        if wins(time, dist, guess) and not wins(time, dist, guess + 1):
            # we found it!!
            endPoint = guess
            print("Found the ending point:", endPoint)
            break
        elif wins(time, dist, guess):
            min = guess + 1
        else:
            max = guess - 1
    return (endPoint - startPoint) + 1


races = getRaces()
total = 1
for race in races:
    total *= waysToWin(race[0], race[1])
print(total)

