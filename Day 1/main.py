def Calories1():
    highest = 0
    current = 0

    with open("input_day1.txt") as file:
        for line in file:
            if line == "\n":
                if current > highest:
                    highest = current
                current = 0
                continue
            current = current + int(line)

    print("Most calories carreid by elf: ",highest)

def Calories2():
    current = 0
    total = 0
    calories = []

    with open("input_day1.txt") as file:
        for line in file:
            if line == "\n":
                calories.append(current)
                current = 0
                continue
            current = current + int(line)

    top = sorted(calories,reverse=True)[:3]

    for i in top:
        total += i

    print("Total calories carried by top 3 elfs: ",total)

Calories1()
Calories2()