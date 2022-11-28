import copy

layout = []
row_count = 0
column_count = 0

def run():
    global layout
    global row_count
    global column_count
    '''
        File input is a plain text file of lines where each line
        a row of characters representing foor (.) or seat L.
    '''
    with open('input') as f:
        lines = f.readlines()
    for line in lines:
        layout.append(list(line.rstrip()))
    row_count = len(layout)
    column_count = len(layout[0])

    iteration = 0
    while True:
        next_layout = copy.deepcopy(layout)
        for (row_idx, row) in enumerate(layout):
            for (column_idx, column) in enumerate(layout[row_idx]):
                '''
                    Process Rules:
                      - Empty seat L and no occupied seats adjacent, becomes occupied #
                      - Occupied seat # and 5+ seats occupied, becomes empty L
                '''
                adjacent = get_seats_adjacent(column_idx, row_idx)
                #print(f'adjacent to {column_idx}, {row_idx}: {adjacent}')
                if column == 'L' and all([True if seat == 'L' else False for seat in adjacent]):  # all adjacent seats vacant
                    next_layout[row_idx][column_idx] = '#'
                if column == '#' and len([seat for seat in adjacent if seat == '#']) >= 5:
                    next_layout[row_idx][column_idx] = 'L'
        # Done computing next_layout, we can stop if it is identical to layout
        #print(f'comparing:\n{layout}\n{next_layout}')
        if layout == next_layout:
            print(f'Think we are done with final layout, returning')
            return
        layout = next_layout
        iteration += 1
        # failsafe
        if iteration > 10000:
            return


def get_seats_adjacent(seat_x, seat_y):
    '''
        "adjacent" has been redefined to be more broad than 8 immediate
        It stretches out in all compass directions over empty spaces until it finds the boundary, L, or #
    '''
    global layout
    global row_count
    global column_count
    seats = []
    vectors = dict(n=(0, -1), ne=(1, -1), e=(1, 0), se=(1, 1), s=(0, 1), sw=(-1, 1), w=(-1, 0), nw=(-1, -1))
    # watch out for range(). The 2nd argument is not inclusive, hence +1
    for (direction, vector) in vectors.items():
        check_x = seat_x + vector[0]
        check_y = seat_y + vector[1]
        while check_x >= 0 and check_y >= 0 and check_x < column_count and check_y < row_count:
            #print(f'checking {check_x} {check_y}')
            if layout[check_y][check_x] != '.':
                seats.append(layout[check_y][check_x])
                break
            check_x += vector[0]
            check_y += vector[1]

    return seats

def print_layout():
    for row in layout:
        print(row, sep=' ')


def get_occupied():
    occupied = 0
    for row in layout:
        occupied += len([seat for seat in row if seat == '#'])
    return occupied

if __name__ == '__main__':
    run()
    print_layout()
    print(f'Seats occupied: {get_occupied()}')
