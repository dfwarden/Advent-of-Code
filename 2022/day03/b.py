'''
- input is line of characters, each indicating different item
- elves are groups of 3, the one common element is their identifier
- a-z have priority 1-26
- A-Z have priority 27-52

order:
- sum the priority of the common element per 3 rows
'''
priority_sum = 0
with open('input', 'r') as f:
    group_index = 0
    sets = [set(), set(), set()]
    for line in f:
        rucksack = line.strip()
        sets[group_index].update(rucksack)
        group_index += 1
        if group_index == 3:  # 3 rows read, calculate intersection
            inall = sets[0].intersection(sets[1], sets[2]).pop()
            if inall.islower():
                priority_sum += ord(inall) - 96
            else:  # uppercase
                priority_sum += ord(inall) - 64 + 26
            group_index = 0
            sets = [set(), set(), set()]


print(f'Afterwards, sum of most common items\' priorites is: {priority_sum}')
