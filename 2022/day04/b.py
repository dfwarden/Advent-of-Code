'''
input is 2 ranges of numbers, separated by comma

how many ranges _at all overlap_?
'''
import re

overlap = 0
pattern = r'([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        matches = re.match(pattern, line)
        elf1 = (int(matches.group(1)), int(matches.group(2)))
        elf2 = (int(matches.group(3)), int(matches.group(4)))
        # in range(start, stop), stop is NOT inclusive, hence the +1s
        if(set(range(elf1[0], elf1[1]+1)) & set(range(elf2[0], elf2[1]+1))):
            overlap += 1

print(f'Afterwards, number of elves with any overlap: {overlap}')

