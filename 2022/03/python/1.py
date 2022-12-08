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
for rucksack in rucksacks:
    firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    common_item = ''.join(set(firstpart).intersection(secondpart))
    priority += values[common_item]

print(priority)
    


