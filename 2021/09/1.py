import numpy as np

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
heightmap = np.array([list(line) for line in input_lines]).astype(int)


def point_is_lowest(array, idx_to_check, point_to_check):
    (point_x, point_y) = idx_to_check
    (x_dim, y_dim) = array.shape
    positions_to_check = [(point_x-1, point_y), (point_x, point_y+1),
                          (point_x+1, point_y), (point_x, point_y-1)]

    if(point_x == 0):
        positions_to_check.remove((point_x-1, point_y))
    if(point_y == 0):
        positions_to_check.remove((point_x, point_y-1))
    if(point_x == x_dim-1):
        positions_to_check.remove((point_x+1, point_y))
    if(point_y == y_dim-1):
        positions_to_check.remove((point_x, point_y+1))

    for (pos_x, pos_y) in positions_to_check:
        adj_point = array[pos_x, pos_y]
        if(adj_point <= point_to_check):
            return False
    return True


low_points = [point for (_, point) in [(idx, point) for (idx, point) in np.ndenumerate(
    heightmap) if point_is_lowest(heightmap, idx, point)]]

print(sum([point+1 for point in low_points]))
