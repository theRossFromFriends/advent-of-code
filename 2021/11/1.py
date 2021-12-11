import numpy as np

fileObj = open('input', "r")
input = fileObj.read().splitlines()
matrix = np.array([list(line) for line in input]).astype(int)


def get_adjacent_octopuses(matrix, octopus):
    (x, y) = octopus
    (x_dim, y_dim) = matrix.shape

    adjacent_octopuses = []
    dx_low = -1 if x > 0 else 0
    dx_high = 1 if x < x_dim-1 else 0
    dy_low = -1 if y > 0 else 0
    dy_high = 1 if y < y_dim-1 else 0
    for dx in range(dx_low, dx_high+1):
        for dy in range(dy_low, dy_high+1):
            if not (dx == 0 and dy == 0):
                adjacent_octopuses.append((x+dx, y+dy))

    return adjacent_octopuses


flashes_total = 0
for i in range(100):
    flashed_in_step = []
    matrix += 1
    matrix[matrix > 9] += 1
    flashing = [(x[0], x[1]) for x in np.argwhere(matrix > 9)]
    [flashed_in_step.append(x) for x in flashing]

    while len(flashing) > 0:
        new_flashing = []
        for flashy_octopus in flashing:
            adj_octopuses = get_adjacent_octopuses(matrix, flashy_octopus)
            for adj_o in adj_octopuses:
                matrix[adj_o] += 1
                if (matrix[adj_o] > 9 and (adj_o not in flashed_in_step)):
                    new_flashing.append(adj_o)
                    flashed_in_step.append(adj_o)
        flashing = new_flashing

    matrix[matrix > 9] = 0
    flashes_total += len(matrix[matrix == 0])

print(flashes_total)
