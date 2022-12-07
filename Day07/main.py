from collections import defaultdict

data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

def DirectoriesSizes():
    filePath = []
    dirSizes = defaultdict(int)

    for line in lines:
        parts = line.strip().split()

        if parts[1] == 'cd':
            if parts[2] == '..':
                filePath.pop()
            else:
                filePath.append(parts[2])
        elif parts[1] == 'ls' or parts[0] == "dir":
            continue
        else:
            size = int(parts[0])
            for i in range(1, len(filePath)+1):
                dirSizes['/'.join(filePath[:i])] += size
   
    answer = 0

    for i, v in dirSizes.items():
        if v <= 100000:
            answer += v
    
    print("Total size of directories <= 100000: ",answer)

    # Part 2

    # Comment for myself if looking for min() we cannot give variable value of 0
    # as there wont be any lower numbers if not counting negative ones.
    answer2 = 99999999
    maxUsage = 70000000 - 30000000
    currentUsage = dirSizes['/']
    needToFree = currentUsage - maxUsage

    for i, v in dirSizes.items():
        if v >= needToFree:
            answer2 = min(answer2, v)
    
    print("Smallest directory size which can be be deleted for update: ", answer2)

DirectoriesSizes()