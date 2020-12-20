import copy


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

    There are too many possibilities to brute force. Need to reduce the possibilities.

    We're looking for a multiplier for each bus to see if (bus * multiplier) - index = T

    This might require math. I think these are coprime.
    '''
    max_value = 100000000000000 * 1000  # hopefully this is big enough
    for multiple in range(busses_sorted[0][1], max_value, busses_sorted[0][1]):
        t_candidate = multiple - busses_sorted[0][0]
        t_found = True
        for (offset, bus) in busses_sorted:
            # if t_candidate + offset % bus == 0, that's good
            if not (t_candidate + offset) % bus == 0:
                t_found = False
        if t_found:
            print(f'found correct t_candidate: {t_candidate}')
            break




if __name__ == '__main__':
    run()
