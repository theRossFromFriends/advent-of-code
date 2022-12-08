import string

fileObj = open('../input.txt', "r")
rucksacks = fileObj.read().split('\n')

# encode the items priority
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

priority = 0
x = iter(rucksacks)
for elf_1, elf_2, elf_3 in zip(x, x, x):
    common_item = ''.join(set(elf_1).intersection(elf_2).intersection(elf_3))
    priority += values[common_item]

print(priority)
    


