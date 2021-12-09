import numpy as np

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
heightmap = np.array([list(line) for line in input_lines]).astype(int)


def get_positions_to_check(x, y, x_dim, y_dim):
    array = [(x-1, y), (x, y+1),
             (x+1, y), (x, y-1)]

    if(x == 0):
        array.remove((x-1, y))
    if(y == 0):
        array.remove((x, y-1))
    if(x == x_dim-1):
        array.remove((x+1, y))
    if(y == y_dim-1):
        array.remove((x, y+1))

    return array


def point_is_lowest(array, idx_to_check, point_to_check):
    (point_x, point_y) = idx_to_check
    (array_x_dim, array_y_dim) = array.shape
    positions_to_check = get_positions_to_check(
        point_x, point_y, array_x_dim, array_y_dim)

    for (pos_x, pos_y) in positions_to_check:
        adj_point = array[pos_x, pos_y]
        if(adj_point <= point_to_check):
            return False
    return True


def point_not_in_basin(x, y, basin_to_check):
    return (len([point for point in basin_to_check if ((point[0][0] == x) and (point[0][1] == y))]) == 0)


low_points = [point for point in [(idx, point) for (idx, point) in np.ndenumerate(
    heightmap) if point_is_lowest(heightmap, idx, point)]]

basin_sizes = []
(x_dim, y_dim) = heightmap.shape
for low_point in low_points:
    basin = [low_point]
    points_to_check = [low_point]
    while(len(points_to_check) > 0):
        new_points_to_check = []
        for point in points_to_check:
            ((point_x, point_y), point_value) = point
            positions_to_check = get_positions_to_check(
                point_x, point_y, x_dim, y_dim)

            for (pos_x, pos_y) in positions_to_check:
                adj_point = heightmap[pos_x, pos_y]
                if((adj_point) > point_value and (adj_point < 9) and point_not_in_basin(pos_x, pos_y, basin)):
                    basin.append(((pos_x, pos_y), adj_point))
                    new_points_to_check.append((
                        (pos_x, pos_y), adj_point))

        points_to_check = new_points_to_check

    size = len(basin)
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)
top_3 = basin_sizes[:3]
result = 1
for size in top_3:
    result *= size
print(result)
