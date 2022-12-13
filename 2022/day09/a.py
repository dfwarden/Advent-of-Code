'''
 - "rope physics" aka "tail follows head" and "input moves head"
 - not given field dimensions ahead of time, 19 is biggest move

 - after all input, how many positions did tail visit at least once?

 - guessing that 200x200 is big enough
 - actually 200x200 is not enough, try 5000x5000
 - processing input:
    - move H
    - recalculate T
    - update visited with T
    - repeat
'''

field = [['' for x in range(5000)] for y in range(5000)]
visited = [[0 for x in range(5000)] for y in range(5000)]
head = {'y': 2500, 'x': 2500}
tail = {'y': 2500, 'x': 2500}
field[head['y']][head['x']] = 'H'  # start at (y, x) (100, 100)
visited[tail['y']][tail['x']] = 1

def is_adjacent(head, tail):
    # absolute sum of difference in coordinates = 2 ONLY for diagonal
    # otherwise, absolute sum of coordinate difference = 1
    if head['x'] == tail['x'] or head['y'] == tail['y']:  # not diagonal
        if abs(head['x'] - tail['x']) + abs(head['y'] - tail['y']) == 1:
            return True
    else:  # diagonal
        if abs(head['x'] - tail['x']) + abs(head['y'] - tail['y']) == 2:
            return True
    return False

def get_new_tail():
    # Easiest situation is if head is in one of the 8 positions around
    # tail: do nothing
    # Otherwise, move one step closer to head is within one of those 8.
    # Caveat: if not in the same row or column, tail always moves diagonally
    if is_adjacent(head, tail):
        return tail
    # not adjacent. If diagonal, move diagonal
    if head['x'] == tail['x'] or head['y'] == tail['y']:  # not diagonal
        # move 1 closer in cardinal direction
        new_y = tail['y'] + ((head['y'] - tail['y'])//2)
        new_x = tail['x'] + ((head['x'] - tail['x'])//2)
        return({'y': new_y, 'x': new_x})
    else:  # diagonal
        # move 1 closer in diagonal direction
        # struggling with the math so calculate the 4 possibilities
        if tail['y'] < head['y'] and tail['x'] > head['x']:  # tail NE
            return({'y': tail['y']+1, 'x': tail['x']-1})
        if tail['y'] > head['y'] and tail['x'] > head['x']:  # tail SE
            return({'y': tail['y']-1, 'x': tail['x']-1})
        if tail['y'] > head['y'] and tail['x'] < head['x']:  # tail SW
            return({'y': tail['y']-1, 'x': tail['x']+1})
        if tail['y'] < head['y'] and tail['x'] < head['x']:  # tail NW
            return({'y': tail['y']+1, 'x': tail['x']+1})

# now read and process input
with open('input', 'r') as f:
    for line in f:
        (direction, distance) = line.rstrip().split(' ')
        distance = int(distance)
        #print(f'processing instruction {direction} {distance}')
        for step in range(distance):
            # unset H, T from current position
            field[head['y']][head['x']] = ''
            field[tail['y']][tail['x']] = ''
            # calculate new H position
            if direction == 'U':  # up
                head['y'] -= 1
            elif direction == 'D':  # down
                head['y'] += 1
            elif direction == 'L':  # left
                head['x'] -= 1
            else:  # right
                head['x'] += 1
            # update field with new H position
            field[head['y']][head['x']] = 'H'
            # recalculate tail T in relation to head H
            tail = get_new_tail()
            # update field with new T position
            field[tail['y']][tail['x']] = 'T'
            #print(f'H({head["y"]}, {head["x"]}) T({tail["y"]}, {tail["x"]}) {is_adjacent(head, tail)}')
            visited[tail['y']][tail['x']] = 1
