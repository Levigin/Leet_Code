def get_island_perimeter(board: list[list[int]]) -> int:
    perimeter = 0
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                perimeter += (4 - len(get_neighs(board, i, j, n, m)))
    return perimeter


def get_neighs(board, i, j, n, m):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighs = []
    for d in delta:
        y, x = i + d[0], j + d[1]
        if 0 <= y < n and 0 <= x < m and board[y][x] == 1:
            neighs.append([y, x])
    print(f'{neighs = }')
    return neighs


def printer(board: list[list[int]]):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == '__main__':
    nums = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    printer(nums)
    print(f'Ans: {get_island_perimeter(nums)}')
