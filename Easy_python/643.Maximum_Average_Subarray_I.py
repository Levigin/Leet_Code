import math


def find_max_average(nums: list[int], k: int) -> float:

    sum_subarray = sum(nums[0:k])
    k1 = k
    max_avg = sum_subarray / k1
    i = 0
    while k < len(nums):
        sum_subarray += nums[k]
        sum_subarray -= nums[i]
        max_avg = max(max_avg, sum_subarray / k1)
        i += 1
        k += 1

    return max_avg


if __name__ == '__main__':
    nums_ = [1,2,3,4,5,6]
    k_ = 2
    print(f'Ans: {find_max_average(nums_, k_)}')
