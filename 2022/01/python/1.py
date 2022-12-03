fileObj = open('../input.txt', "r")
elves = fileObj.read().split('\n\n')

max_total = 0
for elf in elves:
    elf_loads = list(map(int,elf.split('\n')))
    total = sum(elf_loads)
    if(total>max_total):
        max_total = total

print(max_total)