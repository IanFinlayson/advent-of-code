import re

def getInput():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            return lines

def getVal(v):
    match v:
        case "one": return "1"
        case "two": return "2"
        case "three": return "3"
        case "four": return "4"
        case "five": return "5"
        case "six": return "6"
        case "seven": return "7"
        case "eight": return "8"
        case "nine": return "9"

        # this could have been done much better :\
        case "eno": return "1"
        case "owt": return "2"
        case "eerht": return "3"
        case "ruof": return "4"
        case "evif": return "5"
        case "xis": return "6"
        case "neves": return "7"
        case "thgie": return "8"
        case "enin": return "9"

        case _: return str(v)

def searchy(line, rev):
    # this was ugly i tried reversing the string but () screwed me up lol
    ss = "(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
    ssr = "(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)"
    if rev:
        m = re.search(ssr + "|[0-9]", line[::-1])
    else:
        m = re.search(ss + "|[0-9]", line)

    return getVal(m.group(0))

lines = getInput()
total = 0
for line in lines:
    total += int(searchy(line, False) + searchy(line, True))
print(total)

