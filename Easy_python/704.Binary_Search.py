def binary_search(nums: list[int], target: int) -> int:
    def recursive(array: list[int], left_border: int, right_border: int, val: int):
        # base case
        if left_border >= right_border:
            return -1

        m = (right_border + left_border) // 2
        if array[m] == val:
            return m
        if val < array[m]:
            return recursive(array, left_border, m, val)
        else:
            return recursive(array, m + 1, right_border, val)

    return recursive(nums, 0, len(nums), target)


if __name__ == '__main__':
    n = [-1, 0, 3, 5, 9, 12]
    t = 9
    print(f'Ans: {binary_search(n, t)}')
