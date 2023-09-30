def image_smoother(img: list[list[int]]) -> list[list[int]]:
    n, m = len(img), len(img[0])
    mat = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            mat[i][j] = get_avg(i, j, img)

    return mat


def get_avg(y: int, x: int, img: list[list[int]]) -> int:
    delta = [(-1, 0), (1, 0), (-1, 1), (1, -1), (0, -1), (0, 1), (1, 1), (-1, -1)]
    avg = img[y][x]
    counter = 1

    for d in delta:
        y_, x_ = d[0] + y, d[1] + x
        if 0 <= y_ < len(img) and 0 <= x_ < len(img[0]):
            avg += img[y_][x_]
            counter += 1

    return int(avg / counter)


def printer(mat):
    for row in mat:
        for col in row:
            print(f'{col}', end=' ')
        print()


if __name__ == '__main__':
    nums = [[100,200,100],[200,50,200],[100,200,100]]
    print(f'Ans: {printer(image_smoother(nums))}')
