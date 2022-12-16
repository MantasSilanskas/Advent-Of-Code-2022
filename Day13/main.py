data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

def ComparePairs(pair1, pair2):
    # both values are integers.
    if isinstance(pair1, int) and isinstance(pair2, int):
        if pair1 < pair2:
            return -1
        elif pair1 == pair2:
            return 0
        else:
            return 1
    # both values are lists.
    elif isinstance(pair1, list) and isinstance(pair2, list):
        i = 0
        while i < len(pair1) and i < len(pair2):
            c = ComparePairs(pair1[i], pair2[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == len(pair1) and i < len(pair2):
            return -1
        elif i == len(pair2) and i < len(pair1):
            return 1
        else:
            return 0
    # exactly one value is an integer.
    elif isinstance(pair1, int) and isinstance(pair2, list):
        return ComparePairs([pair1], pair2)
    else:
        return ComparePairs(pair1, [pair2])


packets = []

def Part1():
    answer1 = 0
    for i, group in enumerate(data.split('\n\n')):
        pair1, pair2 = group.split('\n')

        pair1 = eval(pair1)
        pair2 = eval(pair2)

        packets.append(pair1)
        packets.append(pair2)

        if ComparePairs(pair1, pair2)==-1:
            answer1 += 1+i

    print("Sum of indixes in pairs: ", answer1)

Part1()

# The distress signal protocol also requires that you include two additional 
# divider packets.
packets.append([[2]])
packets.append([[6]])

def Part2():
    global packets

    from functools import cmp_to_key

    packets = sorted(packets, key=cmp_to_key(lambda p1,p2: ComparePairs(p1,p2)))

    # We need put answer2 at 1 because any multiply of 0 will always be equal to
    # 0.
    answer2 = 1
    for i, p in enumerate(packets):
        if p == [[2]] or p == [[6]]:
            answer2 *= i + 1

    print("Decoder key for distress signal", answer2)

Part2()