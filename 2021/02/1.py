import csv
fileObj = open('input', "r")
lines = fileObj.read().splitlines()

horizon = 0
depth = 0
for i in range(0, len(lines)):
    line = lines[i]
    direction = line.split()[0]
    measure = int(line.split()[1])
    if direction == 'forward':
        horizon += measure
    elif direction == 'up':
        depth -= measure
    elif direction == 'down':
        depth += measure

print(horizon*depth)
