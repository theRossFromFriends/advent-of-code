import numpy as np

fileObj = open('../input.txt', "r")
readData = fileObj.read().split('\n')

heights = []
visibilities = []
for line in readData:
    row = [int(element)
           for element in list(line)]  # 'x' for not visible
    visibility = ['x' for element in list(line)]
    heights.append(row)
    visibilities.append(visibility)
height_array = np.array(heights)
visibility_array = np.array(visibilities)

# iterate over rows
for i, (row_h, row_v) in enumerate(zip(height_array, visibility_array)):
    # from left to right
    previous_tree_height = -1
    for j, (height, visibility) in enumerate(zip(row_h, row_v)):
        if(visibility == 'v'):  # tree already visible from other side
            break
        if(height > previous_tree_height):
            previous_tree_height = height
            visibility_array[i, j] = 'v'  # i-th row, j-th column
        elif (height > previous_tree_height):
            break

    # from right to left
    previous_tree_height = -1
    for j, (height, visibility) in enumerate(zip(reversed(row_h), reversed(row_v))):
        if(visibility == 'v'):  # tree already visible from other side
            break
        if(height > previous_tree_height):
            previous_tree_height = height
            # i-th row, column from the end
            visibility_array[i, len(row_v)-1-j] = 'v'
        elif (height > previous_tree_height):
            break

# iterate over columns
for i, (column_h, column_v) in enumerate(zip(height_array.T, visibility_array.T)):
    # from left to right
    previous_tree_height = -1
    for j, (height, visibility) in enumerate(zip(column_h, column_h)):
        if(visibility == 'v'):  # tree already visible from other side
            break
        if(height > previous_tree_height):
            previous_tree_height = height
            visibility_array[j, i] = 'v'  # transposed column-row
        elif (height > previous_tree_height):
            break

    # from right to left
    previous_tree_height = -1
    for j, (height, visibility) in enumerate(zip(reversed(column_h), reversed(column_h))):
        if(visibility == 'v'):  # tree already visible from other side
            break
        if(height > previous_tree_height):
            previous_tree_height = height
            # transposed column-row from the end
            visibility_array[len(row_v)-1-j, i] = 'v'
        elif (height > previous_tree_height):
            break

print(sum(x == 'v' for y in visibility_array for x in y))
