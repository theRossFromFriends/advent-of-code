import numpy as np
import sys

fileObj = open('input', "r")
crabs = np.array(fileObj.read().split(',')).astype(int)

max_value = max(crabs)
min_fuel = sys.maxint
for crab in range(max_value):
    x = crab
    fuel = sum([abs(x-crab) for crab in crabs])
    if (fuel < min_fuel):
        min_fuel = fuel

print(min_fuel)