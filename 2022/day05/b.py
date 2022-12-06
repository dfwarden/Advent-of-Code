'''
- 9 'stacks', initialized by lines in input
- line of '[S] [Z] [M] [T] [P] [C] [D] [C] [D]' denotes one item in each stack
- line of ' 1   2   3   4   5   6   7   8   9' denotes end of stacks
- then blank line
- then move X from Y to Z, where X is count of boxes to move from Y to Z
- moving multiple crates retains their order
'''
import re

pattern = r'move ([0-9]+) from ([1-9]) to ([1-9])'
stacks = []
for i in range(9):
    stacks.append(list())
init = True
with open('input', 'r') as f:
    for line in f:
        if line.rstrip() == ' 1   2   3   4   5   6   7   8   9':
            # reverse stacks so that pop() removes the oldest/first in
            # and append() adds new elements to the "end"
            for i in range(9):
                stacks[i].reverse()
            init = False
            f.readline()  # throw away the blank line
            continue
        if init:
            for (stack, pos) in enumerate(range(1, 35, 4)):  # check every 4 characters for stack item
                if line[pos] != ' ':
                    stacks[stack].append(line[pos])
        else:
            matches = re.match(pattern, line.rstrip())
            # slice off the desired items
            move = stacks[int(matches.group(2))-1][-int(matches.group(1)):]
            del(stacks[int(matches.group(2))-1][-int(matches.group(1)):])
            for item in move:
                stacks[int(matches.group(3))-1].append(item)

# at this point, all boxes have been moved.
# what is on the top of each stack?
print(''.join(stacks[i].pop() for i in range(9)))



