import numpy as np

fileObj = open('input', "r")
input_data = np.array(fileObj.read().splitlines())

outputs = [z.split() for z in [y[1] for y in [x.split('|') for x in input_data]]]

print(len([x for line in outputs for x in line if (len(x) in [2,3,4,7])]))