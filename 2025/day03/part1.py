
def process(bank):
    # we find the first biggest number (but not last)
    i = 0
    biggest = 0
    while i < len(bank) - 1:
        if bank[i] > bank[biggest]:
            biggest = i
        i += 1

    # now we find the next biggest from there
    i = biggest + 1
    nextbiggest = i
    while i < len(bank):
        if bank[i] > bank[nextbiggest]:
            nextbiggest = i
        i += 1

    #print(bank)
    #print(biggest, nextbiggest)

    # return the number
    return int(bank[biggest] + bank[nextbiggest])


def main():
    total = 0
    while True:
        try:
            bank = input()
            total += process(bank)
        except EOFError:
            break
    print(total)

main()

