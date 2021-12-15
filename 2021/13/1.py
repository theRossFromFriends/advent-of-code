import numpy as np
import helpers

fileObj = open('input', "r")
input_data = fileObj.read().split('\n\n')
dots = np.array([x.split(',')
                 for x in input_data[0].split('\n')]).astype(int)
folds = input_data[1].splitlines()

paper = helpers.get_marked_initial_paper(dots)

first_fold = folds[0]
paper = helpers.fold_paper(first_fold, paper)

print(np.count_nonzero(paper > 0))
