import numpy as np

fileObj = open('input', "r")
input_lines = np.array(fileObj.read().splitlines())
lines_with_characters = [list(line) for line in input_lines]

left_characters = ['(', '[', '{', '<']
right_characters = [')', ']', '}', '>']

corrupted_lines = []
for line in lines_with_characters:
    line_corrupted = False
    stack = []
    for char in line:
        if (char in left_characters):
            stack.append(char)
        else:
            left_char = stack.pop()
            if left_characters.index(left_char) == right_characters.index(char):
                continue
            else:
                line_corrupted = True
                illegal_char = char
                break
    if (line_corrupted):
        corrupted_lines.append((line, illegal_char))

illegal_chars = np.array([x[1] for x in corrupted_lines])
chars_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
z = [chars_dict[illegal_char] for illegal_char in illegal_chars]
print(sum(z))
