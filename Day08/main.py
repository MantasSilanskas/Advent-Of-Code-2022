forest = [list(map(int, line)) for line in open("input.txt").read().splitlines()]

def VisibleTrees():
    trees = 0
    
    for i in range(len(forest)):
        for o in range(len(forest[i])):
            t = forest[i][o]

            if all(forest[i][x] < t for x in range(o)):
                trees += 1
                continue

            if all(forest[i][x] < t for x in range(o + 1, len(forest[i]))):
                trees += 1
                continue

            if all(forest[x][o] < t for x in range(i)):
                trees += 1
                continue

            if all(forest[x][o] < t for x in range(i + 1, len(forest))):
                trees += 1
                continue

    print("Amount of visible trees: ", trees)

def ScenicScore():
    scenicScore = 0

    for i in range(len(forest)):
        for o in range(len(forest[i])):
            t = forest[i][o]
            left = 0
            right = 0
            up = 0 
            down = 0
            
            for x in range(o - 1, -1, -1):
                left += 1
                if forest[i][x] >= t:
                    break

            for x in range(o + 1, len(forest[i])):
                right += 1
                if forest[i][x] >= t:
                    break

            for x in range(i - 1, -1, -1):
                up += 1
                if forest[x][o] >= t:
                    break

            for x in range(i + 1, len(forest)):
                down += 1
                if forest[x][o] >= t:
                    break

            scenicScore = max(scenicScore, left * right * down * up)

    print("Best scenic score: ", scenicScore)

VisibleTrees()
ScenicScore()