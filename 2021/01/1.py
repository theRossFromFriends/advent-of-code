import csv
fileObj = open('input', "r")
lines = fileObj.read().splitlines()

count = 0
for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        count += 1

print(count)
