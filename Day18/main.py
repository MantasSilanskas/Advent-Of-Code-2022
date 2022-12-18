from collections import deque

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

pos = set()
outside = set()
inside = set()

for line in lines:
    x, y, z = line.split(',')
    x, y, z = int(x), int(y), int(z)
    pos.add((x, y, z))


def outside_sides(x, y, z, part):
    if (x, y, z) in outside:
        return True

    if (x, y, z) in inside:
        return False

    seen = set()

    dq = deque([(x, y, z)])

    while dq:
        x, y, z = dq.popleft()

        if (x, y, z) in pos:
            continue

        if (x, y, z) in seen:
            continue

        seen.add((x, y, z))

        if len(seen) > (5000 if part == 2 else 0):
            for p in seen:
                outside.add(p)
            return True

        dq.append((x+1, y, z))
        dq.append((x-1, y, z))
        dq.append((x, y+1, z))
        dq.append((x, y-1, z))
        dq.append((x, y, z+1))
        dq.append((x, y, z-1))

    for p in seen:
        inside.add(p)

    return False


def solve(part):
    outside.clear()
    inside.clear()

    answer = 0
    for (x, y, z) in pos:
        if outside_sides(x + 1, y, z, part):
            answer += 1
        if outside_sides(x - 1, y, z, part):
            answer += 1
        if outside_sides(x, y + 1, z, part):
            answer += 1
        if outside_sides(x, y - 1, z, part):
            answer += 1
        if outside_sides(x, y, z + 1, part):
            answer += 1
        if outside_sides(x, y, z - 1, part):
            answer += 1

    return answer


print("Surface area of scanned lava droplet: ", solve(1))
print("Exterior area of scanned lava droplet: ", solve(2))
