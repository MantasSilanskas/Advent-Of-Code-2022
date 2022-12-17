data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

answer = 0
drawing = [[' ' for _ in range(40)] for _ in range(6)]


def CombinedSignalsStrenght():
    cycle = 0
    x = 1

    for line in lines:
        commands = line.split()
        if commands[0] == 'noop':
            cycle += 1
            handleCycle(cycle, x)
        elif commands[0] == 'addx':
            cycle += 1
            handleCycle(cycle, x)
            cycle += 1
            handleCycle(cycle, x)
            x += int(commands[1])

    print("Total strength of 20th, 60th, 100th, 140th, 180th and 220th cycle signals: ", answer)


def SecretLetters():
    print("Answer of part 2: ")
    for v in range(6):
        print(''.join(drawing[v]))


def handleCycle(cycle, value):
    global answer
    global drawing

    cycle2 = cycle - 1
    drawing[cycle2//40][cycle2 %
                        40] = ('#' if abs(value-(cycle2 % 40)) <= 1 else '.')

    if cycle in [20, 60, 100, 140, 180, 220]:
        answer += value * cycle


CombinedSignalsStrenght()
SecretLetters()
