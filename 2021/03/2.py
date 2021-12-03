import csv
import numpy as np
import copy
fileObj = open('input', "r")
lines_oxygen = np.array(fileObj.read().splitlines())
lines_co2 = copy.deepcopy(lines_oxygen)

oxygen_generator_rating = 0
for i in range(0, len(lines_oxygen[0])):
    bit_count = [0, 0]
    for j in range(0, len(lines_oxygen)):
        line = lines_oxygen[j]
        if line[i] == '0':
            bit_count[0] += 1
        else:
            bit_count[1] += 1

    if bit_count[0] > bit_count[1]:
        lines_oxygen = [x for x in lines_oxygen if x[i] == '0']
    else:
        lines_oxygen = [x for x in lines_oxygen if x[i] == '1']
oxygen_generator_rating = int(lines_oxygen[0], 2)

co2_scrubber_rating = 0
for i in range(0, len(lines_co2[0])):
    bit_count = [0, 0]
    for j in range(0, len(lines_co2)):
        line = lines_co2[j]
        if line[i] == '0':
            bit_count[0] += 1
        else:
            bit_count[1] += 1

    if (bit_count[0] == 0 or bit_count[1] == 0):
        continue

    if bit_count[0] > bit_count[1]:
        lines_co2 = [x for x in lines_co2 if x[i] == '1']
    else:
        lines_co2 = [x for x in lines_co2 if x[i] == '0']
co2_scrubber_rating = int(lines_co2[0], 2)

print(oxygen_generator_rating*co2_scrubber_rating)
