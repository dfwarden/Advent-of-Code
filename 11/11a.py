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
                      - Occupied seat # and 4+ seats occupied, becomes empty L
                '''
                adjacent = get_seats_adjacent(column_idx, row_idx)
                #print(f'adjacent to {column_idx}, {row_idx}: {adjacent}')
                if column == 'L' and all([True if seat == 'L' else False for seat in adjacent]):  # all adjacent seats vacant
                    next_layout[row_idx][column_idx] = '#'
                if column == '#' and len([seat for seat in adjacent if seat == '#']) >= 4:
                    next_layout[row_idx][column_idx] = 'L'
        # Done computing next_layout, we can stop if it is identical to layout
        #print(f'comparing:\n{layout}\n{next_layout}')
        if layout == next_layout:
            print(f'Think we are done with final layout, returning')
            return
        layout = next_layout
        iteration += 1
        if iteration > 10000:
            return


def get_seats_adjacent(seat_x, seat_y):
    global layout
    global row_count
    global column_count
    seats = []
    # watch out for range(). The 2nd argument is not inclusive, hence +1
    for y_check in range(max(0, seat_y - 1), min(row_count, seat_y + 1 + 1)):
        for x_check in range(max(0, seat_x - 1), min(column_count, seat_x + 1 + 1)):
            if not (x_check == seat_x and y_check == seat_y):
                #print(f'checking {x_check} {y_check} in {layout[y_check]}')
                if layout[y_check][x_check] != '.':  # if it is a seat
                    seats.append(layout[y_check][x_check])
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
