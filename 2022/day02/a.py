'''
input structure:
    - column 1: what opponent will play (A = rock, B = paper, C = scissors)
    - column 2: what I should play (X = rock, Y = paper, Z = scissors)

scoring:
    - rock = 1, paper = 2, scissors = 3
    - plus outcome: 0 = lost, 3 = draw, 6 = win
'''
translate = {'X': '🗻', 'Y': '📄', 'Z': '✂', 'A': '🗻', 'B': '📄', 'C': '✂'}
score_base = {'X': 1, 'Y': 2, 'Z': 3}
total_score = 0

def score(opponent, me):
    round_score = 0
    round_score += score_base[me]
    opponent = translate[opponent]
    me = translate[me]
    if me == opponent:  # draw
        return round_score + 3
    if me == '🗻' and opponent == '✂':
        return round_score + 6
    if me == '✂' and opponent == '📄':
        return round_score + 6
    if me == '📄' and opponent == '🗻':
        return round_score + 6
    return round_score

with open('input', 'r') as f:
    for round in f:
        (opponent, me) = round.rstrip().split(' ')
        total_score += score(opponent, me)

