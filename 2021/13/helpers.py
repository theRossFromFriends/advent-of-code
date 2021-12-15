import numpy as np
import matplotlib.pyplot as plt


def get_marked_initial_paper(dots):
    dim = np.amax(dots)
    paper = np.zeros((dim+1, dim+1))
    for (x, y) in dots:
        paper[x, y] = 1

    return paper


def fold_paper(fold, paper):
    value = int(fold.split('=')[1])
    direction = fold.split('=')[0][-1]

    if direction == 'y':
        side_a = paper[:, :value]
        side_b = paper[:, value+1:]
        reverse_b = np.flip(side_b, axis=1)
        (a_x, a_y) = side_a.shape
        (b_x, b_y) = side_b.shape
        if a_y > b_y:
            d = a_y - b_y
            background = np.zeros((a_x, a_y))
            background[:, d:] = reverse_b
            reverse_b = background
        else:
            d = b_y - a_y
            background = np.zeros((b_x, b_y))
            background[:, d:] = side_a
            side_a = background
    else:
        side_a = paper[:value, :]
        side_b = paper[value+1:, :]
        reverse_b = np.flip(side_b, axis=0)
        (a_x, a_y) = side_a.shape
        (b_x, b_y) = side_b.shape
        if a_x > b_x:
            d = a_x - b_x
            background = np.zeros((a_x, a_y))
            background[d:, :] = reverse_b
            reverse_b = background
        else:
            d = b_x - a_x
            background = np.zeros((b_x, b_y))
            background[d:, :] = side_a
            side_a = background

    return (side_a + reverse_b)


def trim_paper(paper):
    nz = np.nonzero(paper)
    paper = paper[nz[0].min():nz[0].max()+1,
                  nz[1].min():nz[1].max()+1]

    return paper


def print_code(paper):
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    _, ax = plt.subplots()
    _, max_val = 0, 1
    ax.matshow(paper, cmap='ocean')

    for i in range(max_val):
        for j in range(max_val):
            c = paper[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    plt.show()
