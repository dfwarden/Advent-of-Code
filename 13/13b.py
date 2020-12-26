import math

def run():
    '''
        File input is a plain text file of lines.

        First line is estimate of earliest timestamp I could board bus departing seaport.
        Second line are bus IDs in service that indicate how often the bus departs the seaport.
    '''
    with open('input') as f:
        lines = f.readlines()
    earliest_departure = int(lines[0])
    # Clean up busses. Split on comma, strip newline
    # Then convert to list of index,int(bus) tuples with no 'x' elements
    # Then sort in reverse order to make searching more efficient
    busses_initial = [bus for bus in lines[1].rstrip().split(',')]
    busses = [(index, int(bus)) for (index, bus) in enumerate(busses_initial) if bus != 'x']
    busses_sorted = sorted(busses, key=lambda tup: tup[1], reverse=True)
    print(busses_sorted)
    '''
    We want to find the earliest timestamp T where each bus
    departs X minutes after T where X is its index in the list of all busses, including 'x'.

    We're looking for a multiplier for each bus to see if (bus * multiplier) - index = T

    This might require math.
    These are all prime, so the least common multiple is these numbers multiplied together.
    But the fact that we want to divide them by different numbers makes things tricky.

    If the offset is greater than the bus, it can be reduced to offset % bus.

    There should be an additional multiplier for each bus to give
    us the best chance of getting the numbers close for the iteration
    multiplier.
    '''
    busses_reduced = [(offset % bus, bus) if offset > bus else (offset, bus) for (offset, bus) in busses_sorted]
    print(f'Reduced busses:\n{busses_reduced}')
    biggest_bus = busses_sorted[0][1]
    for iteration in range(1, 10000000000000):
        if iteration % 100000 == 0:
            print(f'Iteration {iteration}...')
        # First, calculate about how many times each bus goes in to the biggest bus for this iteration
        multipliers = [round((biggest_bus * iteration) / bus) for (offset, bus) in busses_sorted]
        t_candidates = [(multipliers[i] * busses_sorted[i][1]) - busses_sorted[i][0] for i in range(0, len(multipliers))]
        # check candidates
        target = t_candidates[0]
        results = []
        for (i, candidate) in enumerate(t_candidates):
            results.append(candidate == target or candidate - busses_sorted[i][1] == target or candidate + busses_sorted[i][1] == target)
        if all(results):
            print(f'==== SUCCESS ====')
            print(f'Multipliers for iteration {iteration} are:\n{multipliers}')
            print(f'Candidates for iteration {iteration} are:\n{sorted(t_candidates)}')
            return
        #if min(t_candidates) >= 1202161486:
        #    print(f'went too far, quitting. iteration {iteration}')
        #    print(f'Multipliers for iteration {iteration} are:\n{multipliers}')
        #    print(f'Candidates for iteration {iteration} are:\n{sorted(t_candidates)}')
        #    return




if __name__ == '__main__':
    run()
