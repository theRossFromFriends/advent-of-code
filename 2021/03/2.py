import csv
import numpy as np
import copy
fileObj = open('input', "r")
lines = np.array(fileObj.read().splitlines())


def get_rating(input, most_common=True):
    input_copy = copy.deepcopy(input)
    for i in range(0, len(input_copy[0])):
        bit_count = [0, 0]
        for j in range(0, len(input_copy)):
            line = input_copy[j]
            if line[i] == '0':
                bit_count[0] += 1
            else:
                bit_count[1] += 1

        if (bit_count[0] == 0 or bit_count[1] == 0):
            continue

        if bit_count[0] > bit_count[1]:
            if most_common:
                input_copy = [x for x in input_copy if x[i] == '0']
            else:
                input_copy = [x for x in input_copy if x[i] == '1']
        else:
            if most_common:
                input_copy = [x for x in input_copy if x[i] == '1']
            else:
                input_copy = [x for x in input_copy if x[i] == '0']

    return int(input_copy[0], 2)


oxygen_generator_rating = get_rating(lines)
co2_scrubber_rating = get_rating(lines, most_common=False)

print(oxygen_generator_rating*co2_scrubber_rating)
