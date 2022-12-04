elves = [list()]
per_elf_total = [0]
elf_idx = 0
with open('input', 'r') as f:
    for line in f:
        if line == '\n':  # empty line 👉 new elf
            elf_idx += 1
            elves.append(list())
            per_elf_total.append(0)
        else:
            item = int(line)
            elves[elf_idx].append(item)
            per_elf_total[elf_idx] += item
