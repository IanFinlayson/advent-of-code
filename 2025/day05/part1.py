def getInput():
    ranges = []
    ingredients = []
    stage2 = False

    while True:
        try:
            line = input()
            if line == "":
                stage2 = True
            elif not stage2:
                ranges.append(tuple(map(int, line.split("-"))))
            else:
                ingredients.append(int(line))
        except EOFError:
            break
    return ranges, ingredients

def isFresh(ingredient, ranges):
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            return True
    return False

def main():
    fresh = 0
    ranges, ingredients = getInput()
    for ingredient in ingredients:
        if isFresh(ingredient, ranges):
            fresh += 1
    print(fresh)

main()

