import time


def time_(func):
    def wrapper(*args):
        start = time.time()
        run = func(*args)
        end = time.time()
        print(f'\nTime: {(end - start) * 10**3} ms')
        return run
    return wrapper


@time_
def generate_matrix(n: int):

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    def rec(k: int, i: int, j: int, direction: int, level: int, z_: int):

        if k == n * n:
            matrix[j][i] = k
            return

        if k == z_:
            direction += 1
            level += 2
            z_ += (n - level) * 4 - 4

        matrix[j][i] = k

        if i < len(matrix) - direction - 1 and j == 0 + direction:
            rec(k + 1, i + 1, j, direction, level, z_)
        elif j < len(matrix) - direction - 1 and i == len(matrix) - 1 - direction:
            rec(k + 1, i, j + 1, direction, level, z_)
        elif i > 0 + direction and j == len(matrix) - 1 - direction:
            rec(k + 1, i - 1, j, direction, level, z_)
        elif j > 0 + direction and i == 0 + direction:
            rec(k + 1, i, j - 1, direction, level, z_)

    z = n * 4 - 4
    rec(1, 0, 0, 0, 0, z)
    for i_ in matrix:
        for j_ in i_:
            print(j_, end="\t")
        print()

    return matrix


if __name__ == '__main__':
    t = 31
    m = generate_matrix(t)
    # print(f'Ans: {generate_matrix(t)}')
