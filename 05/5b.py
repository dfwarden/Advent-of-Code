from math import ceil,floor

def run():
    '''
        File input is a plain text file of 10-character columns.
        The columns represent binary space partitioning.
    '''
    with open('input') as f:
        lines = f.readlines()
    ids = []
    for line in lines:
        row = 0
        seat = 0
        # first 7 characters are 'F' or 'B' to determine row
        row_min, row_max = 0, 127
        for r in line[:7]:
            if r == 'F':
                row_max = row_max - ceil( (row_max - row_min) / 2 )
            elif r == 'B':
                row_min = row_min + ceil( (row_max - row_min) / 2 )
        # row_min and row_max should be identical and indicate our desired row
        row = row_min
        seat_min, seat_max = 0, 7
        # Next 3 characters are 'L' or 'R' to determine seat
        for s in line[7:-1]:
            if s == 'L':
                seat_max = seat_max - ceil( (seat_max - seat_min) / 2 )
            elif s == 'R':
                seat_min = seat_min + ceil( (seat_max - seat_min) / 2 )
        # seat_min and seat_max should identical and and inciate our desired seat
        seat = seat_min
        ids.append((row * 8) + seat)
    # My seat is the only missing boarding pass.
    # Some seats don't exist on the plane, so they're also missing.
    # There exists seat IDs +1 and -1 from my seat.
    for x in range(8, max(ids)):
        if x not in ids and x-1 in ids and x+1 in ids:
            print(f'I think my id is {x}')


if __name__ == '__main__':
    run()
