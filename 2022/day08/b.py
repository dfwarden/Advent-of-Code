'''
 - 99 x 99 grid
 - cell digit indicates tree height for that cell

 - calculate "scenic score" for each position to find the highest
 - "scenic score" is product of how many trees are visible in each cardinal direction

 - 280800 is too low
 - coordinate (y,x) (52,15) gets that score with components (52, 8, 45, 15)
 '''

grid = []

with open('input', 'r') as f:
    for line in f:
        row = line.rstrip()
        grid.append([int(tree) for tree in row])

scores = []
positions = []
components = []

for y in range(1,98):
    for x in range(1,98):
        tree = grid[y][x]
        # how many visible to north?
        north_count = 0
        for y_north in range(y-1,-1,-1):  # "from one above to the edge of grid"
            north_count += 1
            if grid[y_north][x] >= tree:  # tree blocks view to north, north_count is set
                break

        # how many visible to east?
        east_count = 0
        for x_east in range(x+1,99):  # "from one to east to the edge of grid"
            east_count += 1
            if grid[y][x_east] >= tree:  # tree blocks view to east, east_count is set
                break

        # how many visible to south?
        south_count = 0
        for y_south in range(y+1,99):  # "from one below to the edge of grid"
            south_count += 1
            if grid[y_south][x] >= tree:  # tree blocks view to south, south_count is set
                break

        # how many visible to west?
        west_count = 0
        for x_west in range(x-1,-1,-1):  # "from one west to the edge of grid"
            west_count += 1
            if grid[y][x_west] >= tree:  # tree blocks view to west, west_count is set
                break

        # all _count variables computed, multiply and append to score[]
        scores.append(north_count * east_count * south_count * west_count)
        components.append((north_count, east_count, south_count, west_count))
        positions.append((y,x))

print(max(scores))
