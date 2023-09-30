def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    result = []
    col = 0
    temp = []
    if r * c != (n := len(mat)) * (m := len(mat[0])):
        return mat

    for i in range(n):
        for j in range(m):
            if col == c:
                result.append(temp[:])
                col = 0
                temp = []
            temp.append(mat[i][j])
            col += 1
    if temp:
        result.append(temp[:])

    return result


if __name__ == '__main__':
    mat_ = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(f'Ans: {matrix_reshape(mat_, r, c)}')
