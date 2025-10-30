def getInput():
    games = []
    while True:
        try:
            game = []
            line = input().split(": ")[1]
            pulls = line.split("; ")
            for pull in pulls:
                balls = pull.split(", ")
                r = g = b = 0
                for ball in balls:
                    parts = ball.split(" ")
                    if parts[1] == "red":
                        r = int(parts[0])
                    elif parts[1] == "green":
                        g = int(parts[0])
                    elif parts[1] == "blue":
                        b = int(parts[0])
                game.append((r, g, b))
            games.append(game)
        except EOFError:
            return games

def minBalls(game):
    min_r = min_g = min_b = 0
    for pull in game:
        if pull[0] > min_r: min_r = pull[0]
        if pull[1] > min_g: min_g = pull[1]
        if pull[2] > min_b: min_b = pull[2]
    return (min_r, min_g, min_b)

# do part 2
games = getInput()
gamenum = 1
total = 0
for g in games:
    mbs = minBalls(g)
    total += mbs[0] * mbs[1] * mbs[2]

print(total)

