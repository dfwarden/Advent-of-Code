import copy


def run():
    '''
        File input is a plain text file of lines where each line is
        a compass direction, L (left), R (right), or F (forward)
        followed by an integer indicating magnitude
    '''
    vectors = dict(N=(0, -1), E=(1, 0), S=(0, 1), W=(-1, 0))
    directions = ['N', 'E', 'S', 'W']  # used for calcuating L and R actions
    moves = []
    start_x = 0
    start_y = 0
    start_dir = 'E'
    with open('input') as f:
        lines = f.readlines()
    for line in lines:
        moves.append((line[0], int(line[1:])))
    now_x = 0
    now_y = 0
    now_dir = start_dir
    for (action, value) in moves:
        print(action, value)
        if action in directions:
            now_x += value * vectors[action][0]
            now_y += value * vectors[action][1]
        elif action == 'F':
            now_x += value * vectors[now_dir][0]
            now_y += value * vectors[now_dir][1]
        elif action == 'L':  # rotate `value` degrees coutner-clockwise
            now_dir = directions[(directions.index(now_dir) - int(value / 90)) % 4]
        elif action == 'R':  # rotate `value` degrees clockwise
            now_dir = directions[(directions.index(now_dir) + int(value / 90)) % 4]
    print(f'After starting from 0,0 we ended up at {now_x},{now_y}')
    print(f'Manhattan distance from origin is: {abs(now_x) + abs(now_y)}')



if __name__ == '__main__':
    run()
