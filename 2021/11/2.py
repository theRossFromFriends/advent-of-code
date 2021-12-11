import numpy as np
import helpers

fileObj = open('input', "r")
input = fileObj.read().splitlines()
octopus_matrix = np.array([list(line) for line in input]).astype(int)


synchronized = False
step = 0
while not synchronized:
    step += 1
    octopus_matrix = helpers.take_a_step(octopus_matrix)
    synchronized = True if np.count_nonzero(
        octopus_matrix != 0) == 0 else False

print(step)
