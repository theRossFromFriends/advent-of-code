fileObj = open('../input.txt', "r")
elves = fileObj.read().split('\n\n')

max_total = 0
total_loads = []
for elf in elves:
    elf_loads = list(map(int,elf.split('\n')))
    total = sum(elf_loads)
    total_loads.append(total)

total_loads.sort()
print(sum(total_loads[-3:]))