moves = []

boardDemo = [
    [' '],
    ['Z','N'],
    ['M','C','D'],
    ['P']
    ]

board = [
    [' '],
    ['Z','T','F','R','W','J','G'],
    ['G','W','M'],
    ['J','N','H','G'],
    ['J','R','C','N','W'],
    ['W','F','S','B','G','Q','V','M'],
    ['S','R','T','D','V','W','C'],
    ['H','B','N','C','D','Z','G','V'],
    ['S','J','N','M','G','C'],
    ['G','P','N','W','C','J','D','L'],
]

with open("input.txt") as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split(" "):
            element.append(token)
        moves.append(element)

for move in moves:
    boxes = []

    startStack = int(move[3])
    endStack = int(move[5])

    for times in range(int(move[1])):
        box = board[startStack][-1]
        del(board[startStack][-1])

        boxes.insert(0,box)

    for box in boxes:
        board[endStack].append(box)

solution = ''
for box in board:
    solution += box[-1]

print(solution)