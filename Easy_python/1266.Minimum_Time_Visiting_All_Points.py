def min_time_visit_all_points(points: list[list[int]]) -> int:
    total = 0

    for p in range(len(points) - 1):
        total += max(abs(points[p][0] - points[p + 1][0]), abs(points[p][1] - points[p + 1][1]))
    return total


if __name__ == '__main__':
    arr = [[1, 1], [3, 4], [-1, 0]]
    print(f'Ans: {min_time_visit_all_points(arr)}')
