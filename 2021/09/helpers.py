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
