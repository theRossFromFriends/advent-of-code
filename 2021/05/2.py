import numpy as np

fileObj = open('input', "r")
lines_input = fileObj.read().splitlines()
lines = [(tuple(tuple(int(y) for y in x.split(','))
                for x in z.split('->'))) for z in lines_input]

dimension = max(max(max(lines)))
diagram = np.zeros((dimension+1, dimension+1))

for ((x1, y1), (x2, y2)) in lines:
    if (x1 == x2):
        if (y1 < y2):
            diagram[x1, y1:(y2+1)] += 1
        else:
            diagram[x1, y2:(y1+1)] += 1
    elif (y1 == y2):
        if (x1 < x2):
            diagram[x1:(x2+1), y1] += 1
        else:
            diagram[x2:(x1+1), y1] += 1
    else:
        if (x1 < x2):
            if (y1 < y2):
                for x, y in zip(np.arange(x1, x2+1), np.arange(y1, y2+1)):
                    diagram[x, y] += 1
            else:  # y1 > y2
                for x, y in zip(np.arange(x1, x2+1), np.arange(y2, y1+1)[::-1]):
                    diagram[x, y] += 1
        else:  # x1 > x2
            if (y1 < y2):
                for x, y in zip(np.arange(x2, x1+1)[::-1], np.arange(y1, y2+1)):
                    diagram[x, y] += 1
            else:  # y1 > y2
                for x, y in zip(np.arange(x2, x1+1)[::-1], np.arange(y2, y1+1)[::-1]):
                    diagram[x, y] += 1

print(np.sum(diagram > 1))
