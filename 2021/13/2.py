import numpy as np
import helpers

fileObj = open('input', "r")
input_data = fileObj.read().split('\n\n')
dots = np.array([x.split(',')
                 for x in input_data[0].split('\n')]).astype(int)
folds = input_data[1].splitlines()

paper = helpers.get_marked_initial_paper(dots)

for fold in folds:
    paper = helpers.trim_paper(helpers.fold_paper(fold, paper))

paper = np.flip(paper, axis=1)
paper = np.rot90(paper)
paper[paper > 0] = 1

helpers.print_code(paper)
