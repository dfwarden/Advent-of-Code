'''
input is 2 ranges of numbers, separated by comma

how many ranges are fully contained by the other?
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
        if((elf1[0] <= elf2[0] and elf1[1] >= elf2[1])  # elf1 contains elf2
                or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1])):  # elf2 contains elf1
            overlap += 1

print(f'Afterwards, number of elves fully contained by another: {overlap}')

