import numpy as np
import helpers

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
lines_with_characters = [list(line) for line in input_lines]

corrupted_lines = helpers.get_corrupted_lines(lines_with_characters)

indices = [line[2] for line in corrupted_lines]
indices.sort(reverse=True)
for idx in (indices):
    del lines_with_characters[idx]

completion_character_lines = helpers.get_completion_character_lines(
    lines_with_characters)

scores_dict = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in completion_character_lines:
    score = 0
    for char in line:
        score *= 5
        score += scores_dict[char]
    scores.append(score)
scores.sort()

print(scores[(len(scores)-1)//2])
