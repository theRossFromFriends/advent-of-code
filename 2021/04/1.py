import numpy as np

fileObj = open('input', "r")
lines = fileObj.read().splitlines()
bingo_numbers = np.array(lines[0].split(','))
boards_data = '\n'.join(lines[2:]).split('\n\n')
boards = []
for line in boards_data:
    line.replace('\n', '')
    board = np.reshape(line.split(), (5, 5))
    boards.append(board)


def mark_number(board, number):
    board[board == number] = 'X'
    return


def check_for_winning(board):
    winning = False
    bool_matrix = (board == 'X')
    if ((True in np.all(bool_matrix, axis=0)) or (True in np.all(bool_matrix, axis=1))):
        winning = True
    return winning


def calculate_score(board, number):
    num_sum = sum(int(i) for i in np.nditer(board) if i != 'X')
    score = num_sum * int(number)
    return score


winning_board_idx = -1
for number_idx, number in enumerate(bingo_numbers):
    for board_idx, board in enumerate(boards):
        mark_number(board, number)
        if (check_for_winning(board)):
            winning_board_idx = board_idx
            winning_number_idx = number_idx
            break
    if winning_board_idx >= 0:
        break
winning_board = boards[winning_board_idx]
winning_number = bingo_numbers[winning_number_idx]

print(calculate_score(boards[winning_board_idx], winning_number))
