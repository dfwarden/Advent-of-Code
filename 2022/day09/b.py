'''
 - "rope physics" aka "tail follows head" and "input moves head"
 - not given field dimensions ahead of time, 19 is biggest move
 - new rope is head + 8 intermediate + tail knot
 - all knots follow same movement rules, but updates calculated
   starting with head and continuing

 - after all input, how many positions did tail visit at least once?

 - guessing that 200x200 is big enough
 - actually 200x200 is not enough, try 5000x5000
 - processing input:
    - move H
    - recalculate T
    - update visited with T
    - repeat
'''

visited = [[0 for x in range(5000)] for y in range(5000)]
knots = [{'y': 2500, 'x': 2500} for i in range(10)]
# head is knots[0], tail is knots[9]
visited[knots[9]['y']][knots[9]['x']] = 1

def needs_to_move(knot_a, knot_b):
    # absolute sum of difference in coordinates = 2 ONLY for diagonal
    # otherwise, absolute sum of coordinate difference = 1
    # could also be on the same point, which does not need to move
    if knot_a['y'] == knot_b['y'] and knot_a['x'] == knot_b['x']:  # do not move
        return False
    if knot_a['x'] == knot_b['x'] or knot_a['y'] == knot_b['y']:  # not diagonal
        if abs(knot_a['x'] - knot_b['x']) + abs(knot_a['y'] - knot_b['y']) == 1:
            return False
    else:  # diagonal
        if abs(knot_a['x'] - knot_b['x']) + abs(knot_a['y'] - knot_b['y']) == 2:
            return False
    return True

def get_new_follower_position(leader, follower):
    # Move, if necessary.
    # Caveat: if not in the same row or column, tail always moves diagonally
    if not needs_to_move(leader, follower):
        return follower
    # not adjacent. If diagonal, move diagonal
    if leader['x'] == follower['x'] or leader['y'] == follower['y']:  # not diagonal
        # move 1 closer in cardinal direction
        new_y = follower['y'] + ((leader['y'] - follower['y'])//2)
        new_x = follower['x'] + ((leader['x'] - follower['x'])//2)
        return({'y': new_y, 'x': new_x})
    else:  # diagonal
        # move 1 closer in diagonal direction
        # struggling with the math so calculate the 4 possibilities
        if follower['y'] < leader['y'] and follower['x'] > leader['x']:  # follower NE
            return({'y': follower['y']+1, 'x': follower['x']-1})
        if follower['y'] > leader['y'] and follower['x'] > leader['x']:  # follower SE
            return({'y': follower['y']-1, 'x': follower['x']-1})
        if follower['y'] > leader['y'] and follower['x'] < leader['x']:  # follower SW
            return({'y': follower['y']-1, 'x': follower['x']+1})
        if follower['y'] < leader['y'] and follower['x'] < leader['x']:  # follower NW
            return({'y': follower['y']+1, 'x': follower['x']+1})

# now read and process input
with open('input', 'r') as f:
    for line in f:
        (direction, distance) = line.rstrip().split(' ')
        distance = int(distance)
        for step in range(distance):
            # calculate new head position
            if direction == 'U':  # up
                knots[0]['y'] -= 1
            elif direction == 'D':  # down
                knots[0]['y'] += 1
            elif direction == 'L':  # left
                knots[0]['x'] -= 1
            else:  # right
                knots[0]['x'] += 1
            # recalculate all knots in relation to head, then each other
            for knot_idx in range(1,10):
                knots[knot_idx] = get_new_follower_position(knots[knot_idx-1], knots[knot_idx])
            #print(f'H({head["y"]}, {head["x"]}) T({tail["y"]}, {tail["x"]}) {is_adjacent(head, tail)}')
            visited[knots[9]['y']][knots[9]['x']] = 1
