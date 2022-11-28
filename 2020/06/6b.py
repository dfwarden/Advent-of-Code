from math import ceil,floor

def run():
    '''
        File input is a plain text file of characters representing questions a person answered 'yes' to.
        Groups of responders are separated by empty lines.
    '''
    with open('input') as f:
        lines = f.readlines()
    groups = []
    group = None
    for line in lines:
        if line == '\n':
            if group != None:
                groups.append(group)
                group = None
            continue
        line = line.rstrip()  # remove trailing newline after detecting blank line
        # If `group` is None, we should seed it with the characters in `line`.
        if group is None:
            group = set(line)
            continue
        # _every_ person in the group needs to answer the question to be include in group.
        # This can be determined by taking the set intersection of `group` and `line`.
        group &= set(line)
    total = 0
    for group in groups:
        print(f'distinct characters in {group}: {len(group)}')
        total += len(group)
    print(f'Sum of counts: {total}')


if __name__ == '__main__':
    run()
