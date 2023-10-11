def get_winner(moves: list[list[int]]):
    grid = [[0] * 3 for _ in range(3)]
    counter = 1
    for i, j in moves:
        if counter % 2 == 0:
            grid[i][j] = 'X'
        else:
            grid[i][j] = 'Y'
        if counter > 3 and check_winner(grid):
            return 'A' if counter % 2 != 0 else 'B'
        counter += 1
    print(f'{counter = }')
    if counter < 4:
        return "Pending"
    return 'Draw'


def check_winner(grid: list[list[int]]) -> bool:
    d1 = [grid[i][i] for i in range(3)]
    if len(set(d1)) == 1 and d1[0] != 0:
        return True
    d2 = [grid[3 - i - 1][i] for i in range(3)]
    if len(set(d2)) == 1 and d2[0] != 0:
        return True
    for row in grid:
        if len(set(row)) == 1 and row[0] != 0:
            return True

    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(grid[j][i])
        if len(set(temp)) == 1 and temp[0] != 0:
            return True


if __name__ == '__main__':
    nums = [[0,0],[1,1]]
    print(f'Ans: {get_winner(nums)}')
