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

def possible(total_r, total_g, total_b, game):
    for pull in game:
        if pull[0] > total_r: return False
        if pull[1] > total_g: return False
        if pull[2] > total_b: return False
    return True


# do part 1
games = getInput()
gamenum = 1
total = 0
for g in games:
    if possible(12, 13, 14, g):
        total += gamenum
    gamenum += 1

print(total)

