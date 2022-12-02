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

print(highest)