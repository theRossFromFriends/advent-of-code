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


last_winning_board_idx = -1
for number_idx, number in enumerate(bingo_numbers):
    if len(boards) == 0:
        break
    board_idx_to_delete = []
    for board_idx, board in enumerate(boards):
        mark_number(board, number)
        if (check_for_winning(board)):
            last_winning_board = boards[board_idx]
            last_winning_number = bingo_numbers[number_idx]
            board_idx_to_delete.append(board_idx)
    for i in sorted(board_idx_to_delete, reverse=True):
        del boards[i]

print(calculate_score(last_winning_board, last_winning_number))
