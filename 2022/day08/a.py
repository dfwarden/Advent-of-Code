'''
 - 99 x 99 grid
 - cell digit indicates tree height for that cell

 - how many trees are visible from outside the grid?
 - aka from each non-corner row and column, how far in can you see?
 - aka when you find a local max, trees are not visible until a new max

 - we build a visibility array, where x,y corresponds to that tree position,
   and value is dict of n,e,s,w compass directions for outer edge from which that tree is visible.
 - 1792 is too high
 - 1686 is too low
 '''

grid = []

with open('input', 'r') as f:
    for line in f:
        row = line.rstrip()
        grid.append([int(tree) for tree in row])

visibility = [[set() for j in range(99)] for i in range(99)]

# tree grid and empty visibility grid are built
# remember to scan from all directions (right, down, left, up)


# calculate visibility from west
for y in range(1,98):
    current_max = grid[y][0]
    for x in range(1,98):
        tree = grid[y][x]
        if tree > current_max:  # tree is visible, and new maximum
            visibility[y][x].add('w')
            current_max = tree

# calculate visibility from north
for x in range(1,98):
    current_max = grid[0][x]
    for y in range(1,98):
        tree = grid[y][x]
        if tree > current_max:  # tree is visible, and new maximum
            visibility[y][x].add('n')
            current_max = tree

# calculate visibility from east
for y in range(1,98):
    current_max = grid[y][98]
    for x in range(97,0,-1):
        tree = grid[y][x]
        if tree > current_max:  # tree is visible, and new maximum
            visibility[y][x].add('e')
            current_max = tree

# calculate visibility from south
for x in range(1,98):
    current_max = grid[98][x]
    for y in range(97,0,-1):
        tree = grid[y][x]
        if tree > current_max:  # tree is visible, and new maximum
            visibility[y][x].add('s')
            current_max = tree

# visibility should be calculated.
# Ignoring the corner rows and columns (392), how many inner trees have at least one element in their set?
visible_count = 392
for y in range(1,98):  # 1 - 97
    for x in range(1,98):  # 1 - 97
        if len(visibility[y][x]) > 0:
            visible_count += 1

print(f'{visible_count} trees visible')
