import numpy as np

fileObj = open('input', "r")
fish = np.array(fileObj.read().split(',')).astype(int)

for i in range(0, 80):
    new_fish_number = np.count_nonzero(fish == 0)
    new_fish = (np.ones(new_fish_number)*8).astype(int)
    fish[fish == 0] = 100
    fish[fish > 0] -= 1
    fish[fish == 99] = 6
    fish = np.append(fish, new_fish)

print(len(fish))
