import numpy as np

fileObj = open('../input.txt', "r")
readData = fileObj.read().split('\n')

heights = []
scenic_scores = []
for line in readData:
    heights_row = [int(element)
                   for element in list(line)]
    scenic_score_row = [1 for element in list(line)]
    heights.append(heights_row)
    scenic_scores.append(scenic_score_row)
height_array = np.array(heights)
scenic_scores_array = np.array(scenic_scores)

for (x, y), height in np.ndenumerate(height_array):
    scenic_score = 1
    trees_in_line = 0
    for i in reversed(range(0, x)):
        trees_in_line += 1
        if(height_array[i, y] >= height):
            break
    scenic_score *= trees_in_line

    trees_in_line = 0
    for i in reversed(range(0, y)):
        trees_in_line += 1
        if(height_array[x, i] >= height):
            break
    scenic_score *= trees_in_line

    trees_in_line = 0
    for i in range(x+1, len(height_array)):
        trees_in_line += 1
        if(height_array[i, y] >= height):
            break
    scenic_score *= trees_in_line

    trees_in_line = 0
    for i in range(y+1, len(height_array.T)):
        trees_in_line += 1
        if(height_array[x, i] >= height):
            break
    scenic_score *= trees_in_line

    scenic_scores_array[x, y] = scenic_score

print(max(map(max, scenic_scores_array)))
