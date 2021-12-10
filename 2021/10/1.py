import numpy as np
import helpers

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
lines_with_characters = [list(line) for line in input_lines]

corrupted_lines = helpers.get_corrupted_lines(lines_with_characters)

illegal_chars = np.array([x[1] for x in corrupted_lines])
chars_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores = [chars_dict[illegal_char] for illegal_char in illegal_chars]

print(sum(scores))
