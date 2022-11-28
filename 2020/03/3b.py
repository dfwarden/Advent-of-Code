import math

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
    max_x = len(lines[0])
    max_y = len(lines)
    # Tuples represent movement increments in (x, y) format.
    increments = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    iteration_results = []
    print(f'{max_y} lines, each {max_x} characters wide (including newline).')
    for (x_increment, y_increment) in increments:
        (you_x, you_y) = (0, 0)
        trees_seen = 0
        while you_y < max_y:
            if lines[you_y][you_x] == '#':
                trees_seen += 1
            you_y += y_increment
            # If you would move beyond column 31, loop back around to column 0.
            you_x = (you_x + x_increment) % 31
        iteration_results.append(trees_seen)
    print(f'Results from each run are: {iteration_results}, they multiply to {math.prod(iteration_results)}.')


if __name__ == '__main__':
    run()
