def ReadFileByLine(fileName, lines):
    lines = []
    with open(fileName) as file:
        for line in file:
            lines.append(line)

    return lines


def SortAscending(list):
    return sorted(list)


def SortDescending(list):
    return sorted(list, reverse=True)


def SplitStringInHalf(string):
    s1 = string[:len(string)//2]
    s2 = string[len(string)//2:]

    return s1, s2


def FindSharedSymbol(string, string2):
    for symbol in string:
        if symbol in string2:
            return symbol
