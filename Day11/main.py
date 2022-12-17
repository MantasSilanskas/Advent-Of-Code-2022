from copy import deepcopy

data = open('input.txt').read().strip()

itemsList = []
operations = []
testCases = []
trueCases = []
falseCases = []


def InputParsing():
    for monkey in data.split('\n\n'):
        _, items, operation, test, trueCase, falseCase = monkey.split('\n')

        itemsList.append([int(i) for i in items.split(':')[1].split(',')])

        commands = operation.split()
        oprt = ''.join(commands[-3:])

        operations.append(lambda old, oprt=oprt: eval(oprt))

        testCases.append(int(test.split()[-1]))

        trueCases.append(int(trueCase.split()[-1]))

        falseCases.append(int(falseCase.split()[-1]))


def MostActiveMonkeys():
    modulo = 1
    for x in testCases:
        modulo = (modulo * x)

    for part in [1]:
        count = [0 for _ in range(len(itemsList))]
        monkey = deepcopy(startPoint)
        for t in range(20 if part == 1 else 10000):
            for i in range(len(monkey)):
                print(monkey)
                for item in monkey[i]:
                    print(item)
                    count[i] += 1
                    item = operations[i](item)

                    if part == 2:
                        item = item % modulo

                    if part == 1:
                        item = item // 3

                    if item % testCases[i] == 0:
                        monkey[trueCases[i]].append(item)
                    else:
                        monkey[falseCases[i]].append(item)
                monkey[i] = []

        print("Part ", part, "answer: ", sorted(count)[-1] * sorted(count)[-2])


InputParsing()

startPoint = deepcopy(itemsList)

MostActiveMonkeys()
