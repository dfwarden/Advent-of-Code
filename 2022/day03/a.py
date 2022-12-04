'''
- input is line of characters, each indicating different item
- items are evenly distributed (first and second half of line)
- a-z have priority 1-26
- A-Z have priority 27-52

order:
- find the type that ocurrs in both halves
- sum the priority of that type in all rows
'''
priority_sum = 0
with open('input', 'r') as f:
    for rucksack in f:
        rucksack = rucksack.strip()
        midpoint = len(rucksack)//2  # floor divide
        compartment1 = set(rucksack[0:midpoint])
        compartment2 = set(rucksack[midpoint:])
        inboth = compartment1.intersection(compartment2).pop()
        if inboth.islower():
            priority_sum += ord(inboth) - 96
        else:  # uppercase
            priority_sum += ord(inboth) - 64 + 26

print(f'Afterwards, sum of most common items\' priorites is: {priority_sum}')
