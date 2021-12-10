import numpy as np
import helpers

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
heightmap = np.array([list(line) for line in input_lines]).astype(int)


low_points = [point for (_, point) in [(idx, point) for (idx, point) in np.ndenumerate(
    heightmap) if helpers.point_is_lowest(heightmap, idx, point)]]

print(sum([point+1 for point in low_points]))
