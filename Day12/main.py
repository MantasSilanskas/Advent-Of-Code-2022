from collections import deque

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

area = []
for line in lines:
    area.append(line)

FixedArea = [[0 for _ in range(len(area[0]))]for _ in range(len(area))]
for l in range(len(area)):
    for s in range(len(area[0])):
        if area[l][s] == 'S':
            FixedArea[l][s] = 1
        elif area[l][s] == 'E':
            FixedArea[l][s] = 26
        else:
           FixedArea[l][s] = ord(area[l][s]) - ord('a') + 1

def FewestSteps():
    DQ = deque()
    S = set()

    for l in range(len(area)):
        for s in range(len(area[0])):
            if area[l][s] == 'S':
                DQ.append(((l,s),0))

    while DQ:
        (l, s), count = DQ.popleft()

        if (l, s) in S:
            continue
        S.add((l,s))

        if area[l][s] == 'E':
            return count

        for ml, ms in [(-1,0),(1,0),(0,-1),(0,1)]:
            ll = l + ml
            ss = s + ms

            if 0 <= ll < len(area) and 0 <= ss < len(area[0]) and FixedArea[ll][ss] <= 1 + FixedArea[l][s]:
                DQ.append(((ll, ss), count + 1))
            
print(FewestSteps())