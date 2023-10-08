def odd_cells(m: int, n: int, indices: list[list[int]]) -> int:
    mat = [[0 for i in range(n)] for j in range(m)]
    res = 0
    for point in indices:
        y, x = point
        i = 0
        while i < len(mat[0]):
            mat[y][i] += 1
            if mat[y][i] % 2 != 0:
                res += 1
            else:
                res -= 1
            i += 1

        j = 0
        while j < len(mat):
            mat[j][x] += 1
            if mat[j][x] % 2 != 0:
                res += 1
            else:
                res -= 1
            j += 1

    return res


if __name__ == '__main__':
    c, v = 2, 2
    nums = [[0, 0], [1, 1]]
    print(f'Ans: {odd_cells(c, v, nums)}')
