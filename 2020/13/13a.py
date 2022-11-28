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
    busses = [int(bus) for bus in lines[1].rstrip().split(',') if bus != 'x']
    wait_times = []  # index matches busses
    for bus in busses:
        wait_counter = earliest_departure
        while True:
            if wait_counter % bus == 0:
                wait_times.append(wait_counter)
                break
            wait_counter += 1
    # `wait_times` should now have the minutes necessary to wait for each bus
    # The bus with the shortest wait has the same index as the smallest value
    # in wait_times
    best_departure = min(wait_times)
    best_bus = busses[wait_times.index(best_departure)]
    print(f'Best bus multiplied by wait time: {best_bus * (best_departure - earliest_departure)}')




if __name__ == '__main__':
    run()
