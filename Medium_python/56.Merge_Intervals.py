def merge_interval(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans


if __name__ == '__main__':
    nums = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4], [1, 7]]
    print(f'Ans: {merge_interval(nums)}')
