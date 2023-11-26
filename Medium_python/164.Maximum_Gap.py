import time
import random


def get_maximum_gap(nums: list[int]):
    if len(nums) < 2:
        return 0

    def radix_sort(arr: list[int]):

        max_digit = max(len(str(_)) for _ in arr)
        new_arr = [[] for _ in range(10)]

        for i in range(max_digit):
            for val in arr:
                digit = (val // 10 ** i) % 10
                new_arr[digit].append(val)
            arr = [j for sub_arr in new_arr for j in sub_arr]
            new_arr = [[] for _ in range(10)]
        return arr

    arr_ = radix_sort(nums)
    max_val = -1
    for i in range(len(arr_) - 1):
        max_val = max(max_val, arr_[i + 1] - arr_[i])

    # Check Radix sort VS Quick sort in python system:
    sort_arr = []
    for i in range(100_0000):
        sort_arr.append(random.randint(0, 100_000_000))

    start = time.time_ns()
    sort_arr.sort()
    end = time.time_ns()
    print(f'Time: {(end - start) // 10 ** 6} ms')
    # Very bad(
    start = time.time_ns()
    radix_sort(sort_arr)
    end = time.time_ns()
    print(f'Time: {(end - start) // 10 ** 6} ms')

    return max_val


if __name__ == '__main__':
    nums_ = [1, 3, 6, 9]
    print(f'Ans: {get_maximum_gap(nums_)}')
