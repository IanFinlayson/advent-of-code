position = 50
times = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    direction = line[0]
    amount = int(line[1:])

    while amount > 0:
        if direction == 'L':
            position -= 1
            if position == -1:
                position = 99
        elif direction == 'R':
            position += 1
            if position == 100:
                position = 0
        amount -= 1

    print("Position is", position)
    if position == 0:
        times += 1

print(times)



