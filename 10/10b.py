import math

def run():
    '''
        File input is a plain text file of lines where each line
        is an integer.

        Each line represents a jolt rating of a charger.

        How many combinations of chargers can get us from 0 to
        max of input + 3?
    '''
    adapters = []
    with open('input') as f:
        lines = f.readlines()
    for line in lines:
        adapters.append(int(line))
    adapters = sorted(adapters)
    target = max(adapters) + 3
    print(f'adapters: {adapters}\ntarget: {target}')
    # for each adapter, count how many possible adapters we could go to next
    next_adapters = []
    for adapter in adapters:
        candidates = [next_adapter for next_adapter in adapters if next_adapter > adapter and next_adapter <= adapter + 3]
        print(f'for {adapter}, next candidates are {candidates}')
        if len(candidates) > 1:
            for candidate in candidates:
                print(f'candidate chain: {adapters[adapters.index(candidate):]}')



  # Maybe from the opposite direction?




if __name__ == '__main__':
    run()
