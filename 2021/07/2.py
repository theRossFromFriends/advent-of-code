import numpy as np
import sys

fileObj = open('input', "r")
crabs = np.array(fileObj.read().split(',')).astype(int)

def calculate_fuel(dist):
    fuel_unit = 0
    unit = 0
    for i in range(1, dist+1):
        unit += 1
        fuel_unit += unit
    return fuel_unit

max_value = max(crabs)
fuel_dict = {distance: calculate_fuel(distance) for distance in range(max_value+1)}

min_fuel = sys.maxint
for crab in range(max_value):
    x = crab
    fuel = sum([fuel_dict[y] for y in [abs(x-crabby) for crabby in crabs]])
    if (fuel < min_fuel):
        min_fuel = fuel

print(min_fuel)