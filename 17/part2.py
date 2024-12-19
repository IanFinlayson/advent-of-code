correct =[2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 1, 5, 5, 3, 0]

octals = []


last = 0
for i in range(16):
    for thing in range(8):
        if ((thing ^ 6) ^ last) == correct[i]:
            octals.append(thing)
            last = thing
            break
octals.reverse()

def toBinary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    while len(binary) < 3:
        binary = "0" + binary
    return binary
    
fullbinary = ""
for o in octals:
    fullbinary += toBinary(o)

print(fullbinary)









