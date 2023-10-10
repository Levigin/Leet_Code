def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    temp = []
    m, n = len(grid), len(grid[0])
    for row in grid:
        temp += row

    length = k % (m * n)
    res = temp[-length:] + temp[: -length]
    ans = []
    for i in range(0, m * n, n):
        ans.append(res[i: i + n])

    return ans


if __name__ == '__main__':
    matrix = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    s = 4
    print(f'Ans: {shift_grid(matrix, s)}')
