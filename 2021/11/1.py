import numpy as np
import helpers

fileObj = open('input', "r")
input = fileObj.read().splitlines()
octopus_matrix = np.array([list(line) for line in input]).astype(int)


flashes_total = 0
for i in range(100):
    octopus_matrix = helpers.take_a_step(octopus_matrix)
    flashes_total += len(octopus_matrix[octopus_matrix == 0])

print(flashes_total)
