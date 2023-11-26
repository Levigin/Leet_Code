def contains_near_by_almost_duplicate(nums: list[int], index_diff: int, value_diff: int) -> bool:
    if value_diff < 0:
        return False

    seen = {}
    for i, x in enumerate(nums):
        bkt = x // (value_diff + 1)
        if bkt in seen and i - seen[bkt][0] <= index_diff:
            return True
        if bkt - 1 in seen and i - seen[bkt - 1][0] <= index_diff and abs(x - seen[bkt - 1][1]) <= value_diff:
            return True
        if bkt + 1 in seen and i - seen[bkt + 1][0] <= index_diff and abs(x - seen[bkt + 1][1]) <= value_diff:
            return True
        seen[bkt] = (i, x)
    return False


if __name__ == '__main__':
    nums_ = [1, 9, 5, 5, 1, 9]
    index = 3
    value = 0
    print(f'Ans: {contains_near_by_almost_duplicate(nums_, index, value)}')
