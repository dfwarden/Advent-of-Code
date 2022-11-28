import copy


def run():
    '''
        File input is a plain text file of lines where each line is
        a compass direction, L (left), R (right), or F (forward)
        followed by an integer indicating magnitude

        In 12b we're not moving the ship, we're moving a waypoint,
        And F actions move the ship in the vector from ship to waypoint.
        L and R rotate waypoint around ship.
        Rotation example: waypoint 10,4 rotated R 90 the new waypoint 4, -10

        Waypoint starts at (10, 1) if origin is (0, 0).
        Waypoint moves relative to ship.
    '''
    vectors = dict(N=(0, 1), E=(1, 0), S=(0, -1), W=(-1, 0))
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
    waypoint_x = 10
    waypoint_y = 1
    for (action, value) in moves:
        print(action, value)
        if action in directions:
            waypoint_x += value * vectors[action][0]
            waypoint_y += value * vectors[action][1]
        elif action == 'F':
            now_x += value * waypoint_x
            now_y += value * waypoint_y
        elif action in ['L', 'R']:
            (waypoint_x, waypoint_y) = rotate_waypoint(action, value, waypoint_x, waypoint_y)
        print(f'ship now at {now_x} {now_y} and waypoint {waypoint_x} {waypoint_y}')
    print(f'After starting from 0,0 we ended up at {now_x},{now_y}')
    print(f'Manhattan distance from origin is: {abs(now_x) + abs(now_y)}')


def rotate_waypoint(action, value, waypoint_x, waypoint_y):
    '''
    Not sure if there's a better way to rotate, but we can break up in to 4 quadrants
    and process the new values based on that.

    Testing:
    R: new_x gets  now_y, new_y gets -now_x
    L: new_x gets -now_y, new_y gets  now_x
    '''
    for step in range(0, int(value / 90)):
        if action == 'R':
            (waypoint_x, waypoint_y) = (waypoint_y, -waypoint_x)
        else:
            (waypoint_x, waypoint_y) = (-waypoint_y, waypoint_x)
    return (waypoint_x, waypoint_y)

if __name__ == '__main__':
    run()
