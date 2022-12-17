data = open('demo.txt').read().strip()
lines = [x for x in data.split('\n')]

M = set()


for line in lines:
    last = None

    for point in line.split('->'):
        x, y = point.split(',')

        x = int(x)
        y = int(y)

        if last is not None:
            dx = x - last[0]
            dy = y - last[1]

            len_ = max(abs(dx), abs(dy))
            for i in range(len_+1):
                xx = last[0] + i * (1 if dx>0 else (-1 if dx<0 else 0))
                yy = last[1] + i * (1 if dy>0 else (-1 if dy<0 else 0))
                
                M.add((xx,yy))

        last = (x,y)

floor = 2 + max(r[1] for r in M)

minX = min(r[0] for r in M) - 2000
maxX = max(r[0] for r in M) + 2000

for x in range(minX, maxX):
    M.add((x, floor))

part1Done = False
for sandUnit in range(1000000):
    rock = (500,0)

    while True:
        if rock[1] + 1 >= floor and (not part1Done):
            part1Done = True
            print('Sand units before it starts to flow into abyss: ', sandUnit)
        if (rock[0], rock[1] + 1) not in M:
            rock = (rock[0], rock[1] + 1)
        elif (rock[0] - 1, rock[1] + 1) not in M:
            rock = (rock[0] - 1, rock[1] + 1)
        elif (rock[0] + 1, rock[1] + 1) not in M:
            rock = (rock[0] + 1, rock[1] + 1)
        else:
            break

    if rock == (500,0):
        print('Sand units before source of sands becomes blocked: ', sandUnit + 1)
        break

    M.add(rock)