def getRaces():
    races = []
    times = list(map(int, input().split()[1:]))
    dists = list(map(int, input().split()[1:]))
    for i in range(len(times)):
        races.append((times[i], dists[i]))
    return races

def waysToWin(time, dist):
    ways = 0
    for i in range(time + 1):
        # charge it for i seconds
        speed = i
        travelled = (time - i) * speed
        if travelled > dist:
            ways += 1
    print("For", time, dist, "we have", ways, "ways to win.")
    return ways

races = getRaces()
total = 1
for race in races:
    total *= waysToWin(race[0], race[1])
print(total)

