def is_valid_sudoku(board: list):
    for i in range(len(board)):
        if not check_line(board[i]) or not check_line([row[i] for row in board]) or\
                not check_line([j for cell in board[(i // 3) * 3: ((i // 3) + 1) * 3] for j in cell[(i % 3) * 3: ((i% 3) +1) * 3]]):
            return False

    return True


def check_line(line: list):
    if len(set(line)) - 1 != 9 - line.count('.'):
        return False
    return True


if __name__ == '__main__':
    board_ = [
        [".", ".", ".", ".", ".", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", "3", ".", ".", "2", ".", "4", ".", "."],
        [".", ".", "7", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", "4", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "."],
        [".", ".", ".", ".", ".", "5", "2", ".", "."]]

    print(f'{is_valid_sudoku(board_)}')
