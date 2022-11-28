def run():
    '''
        File input is a plain text file of lines 31 characters long.
        Each character is a . for open space or # for a tree.
        Starting from position 0,0 (top left) and moving right 3, down 1,
        how many # characters would you encounter?
        Once you move beyond x=31, repeat the first 31 columns.
    '''
    with open('input') as f:
        lines = f.readlines()
    (you_x, you_y) = (0, 0)
    max_x = len(lines[0])
    max_y = len(lines)
    trees_seen = 0
    print(f'{max_y} lines, each {max_x} characters wide (including newline).')
    while you_y < max_y:
        if lines[you_y][you_x] == '#':
            trees_seen += 1
        you_y += 1
        # If you would move beyond column 31, loop back around to column 0.
        you_x = (you_x + 3) % 31
    print(f'You would encounter {trees_seen} trees.')


if __name__ == '__main__':
    run()
