from math import ceil,floor

def run():
    '''
        File input is a plain text file of characters representing questions a person answered 'yes' to.
        Groups of responders are separated by empty lines.
    '''
    with open('input') as f:
        lines = f.readlines()
    groups = []
    group = set()
    for line in lines:
        if line == '\n':
            if group != set():
                groups.append(group)
                group = set()
            continue
        for char in line.rstrip():
            group.add(char)
    total = 0
    for group in groups:
        print(f'distinct characters in {group}: {len(group)}')
        total += len(group)
    print(f'Sum of counts: {total}')



if __name__ == '__main__':
    run()
