# Opponent plays:
# A for rock 
# B for paper
# C for scissors

# Respones:
# X for rock
# Y for paper
# Z for scissors

# Scores for winning:
# 1 for rock
# 2 for paper
# 3 for scissors
# + 0 for losing, 3 for draw and 6 for win
      
# W - win, D - draft, L - lose
def RockPaperScissors1(e, y):
    outcome = ""
    score = 0
    joint = e + y

    if y == "X":
        score += 1
    elif y == "Y":
        score += 2
    elif y == "Z":
        score += 3
    
    if joint == "AX":
        outcome = "D"
    elif joint == "AY":
        outcome = "W"
    elif joint == "AZ":
        outcome = "L"
    elif joint == "BY":
        outcome = "D"
    elif joint == "BX":
        outcome = "L"
    elif joint == "BZ":
        outcome = "W"
    elif joint == "CZ":
        outcome = "D"
    elif joint == "CX":
        outcome = "W"
    elif joint == "CY":
        outcome = "L"

    if outcome == "W":
        score += 6
    elif outcome == "L":
        score += 0
    elif outcome == "D":
        score += 3
    
    return score

def RockPaperScissors2(e, y):
    joint = e + y

    # # (A rock) X(lose) = 0, Y(draw) = 3, Z(win) = 6. Rock + 1, Paper + 2, Scissors + 3
    if joint == "AX":
        score = 3
        return score
    
    if joint == "AY":
        score = 4
        return score

    if joint == "AZ":
        score = 8
        return score

    # # (B paper) X(lose) = 0, Y(draw) = 3, Z(win) = 6. Rock + 1, Paper + 2, Scissors + 3
    if joint == "BX":
        score = 1
        return score
    
    if joint == "BY":
        score = 5
        return score

    if joint == "BZ":
        score =  9
        return score

    # # (C scissors) X(lose) = 0, Y(draw) = 3, Z(win) = 6. Rock + 1, Paper + 2, Scissors + 3
    if joint == "CX":
        score = 2
        return score 
    
    if joint == "CY":
        score = 6
        return score

    if joint == "CZ":
        score = 7
        return score

totalScore1 = 0
totalScore2 = 0
with open("input_day2.txt") as file:
    for line in file:
       totalScore1 += RockPaperScissors1(line[0], line[2])
       totalScore2 += RockPaperScissors2(line[0], line[2])

    print("Part one:" ,totalScore1)
    print("Part two:" ,totalScore2)
