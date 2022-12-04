'''
input structure:
    - column 1: what opponent will play (A = rock, B = paper, C = scissors)
    - column 2: what I should play (X = rock, Y = paper, Z = scissors)

scoring:
    - rock = 1, paper = 2, scissors = 3
    - plus outcome: 0 = lost, 3 = draw, 6 = win
'''
translate = {'X': '🗻', 'Y': '📄', 'Z': '✂', 'A': '🗻', 'B': '📄', 'C': '✂'}
score_base = {'🗻': 1, '📄': 2, '✂': 3}
total_score = 0

def score(opponent, outcome):
    round_score = 0
    opponent = translate[opponent]
    if outcome == 'X':  # need to lose
        if opponent == '📄':
            round_score += 1
        if opponent == '🗻':
            round_score += 3
        if opponent == '✂':
            round_score += 2
    if outcome == 'Y':  # need to tie (play same as opponent)
        round_score += score_base[opponent]
        round_score += 3
    if outcome == 'Z':  # need to win
        round_score += 6
        if opponent == '📄':
            round_score += 3
        if opponent == '🗻':
            round_score += 2
        if opponent == '✂':
            round_score += 1
    return round_score

with open('input', 'r') as f:
    for round in f:
        (opponent, me) = round.rstrip().split(' ')
        total_score += score(opponent, me)

