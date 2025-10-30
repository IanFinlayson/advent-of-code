
total = 0
while True:
    try:
        line = input()
        for c in line:
            if c >= '0' and c <= '9':
                first = c
                break
        for c in reversed(line):
            if c >= '0' and c <= '9':
                last = c
                break
        total += int(first + last)

    except EOFError:
        print(total)
        break




