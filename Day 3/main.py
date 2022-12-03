priorities = [
    ["a", 1],
    ["b", 2],
    ["c", 3],
    ["d", 4],
    ["e", 5],
    ["f", 6],
    ["g", 7],
    ["h", 8],
    ["i", 9],
    ["j", 10],
    ["k", 11],
    ["l", 12],
    ["m", 13],
    ["n", 14],
    ["o", 15],
    ["p", 16],
    ["q", 17],
    ["r", 18],
    ["s", 19],
    ["t", 20],
    ["u", 21],
    ["v", 22],
    ["w", 23],
    ["x", 24],
    ["y", 25],
    ["z", 26],
    ["A", 27],
    ["B", 28],
    ["C", 29],
    ["D", 30],
    ["E", 31],
    ["F", 32],
    ["G", 33],
    ["H", 34],
    ["I", 35],
    ["J", 36],
    ["K", 37],
    ["L", 38],
    ["M", 39],
    ["N", 40],
    ["O", 41],
    ["P", 42],
    ["Q", 43],
    ["R", 44],
    ["S", 45],
    ["T", 46],
    ["U", 47],
    ["V", 48],
    ["W", 49],
    ["X", 50],
    ["Y", 51],
    ["Z", 52],
]


def PrioritiesSum(line):
    compartmentOne = line[:len(line)//2]
    compartmentTwo = line[len(line)//2:]

    for symbol in compartmentOne:
        for symbol2 in compartmentTwo:
            if symbol == symbol2:
                for priority in priorities:
                    if priority[0] == symbol2:
                        return priority[1]


def BadgesProblem(lines):
    line1 = lines[0]
    line2 = lines[1]
    line3 = lines[2]

    for s1 in line1:
        for s2 in line2:
            for s3 in line3:
                if s1 == s2 and s1 == s3 and s2 == s3:
                    for priority in priorities:
                        if priority[0] == s1:
                            return priority[1]


sum = 0
with open("input_day3.txt") as file:
    for line in file:
        sum += PrioritiesSum(line)

print("Total priority of duplicate items in task 1:", sum)

sum2 = 0
with open("input_day3.txt") as file:
    lines = []
    for line in file:
        lines.append(line)
        if len(lines) == 3:
            sum2 += BadgesProblem(lines)
            lines = []

print("Total priority of group items in task 2:", sum2)
