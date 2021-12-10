import numpy as np


def get_corrupted_lines(input):
    left_characters = ['(', '[', '{', '<']
    right_characters = [')', ']', '}', '>']
    corrupted_lines = []
    for (idx, line) in enumerate(input):
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
            corrupted_lines.append((line, illegal_char, idx))

    return corrupted_lines


def get_completion_character_lines(input):
    left_characters = ['(', '[', '{', '<']
    right_characters = [')', ']', '}', '>']
    completion_character_lines = []
    for line in input:
        stack = []
        for char in line:
            if (char in left_characters):
                stack.append(char)
            else:
                stack.pop()
        stack.reverse()

        completion_characters = [right_characters[idx] for idx in [
            left_characters.index(char) for char in stack]]
        completion_character_lines.append(completion_characters)

    return completion_character_lines
