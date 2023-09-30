import math


def maximum_product(nums: list[int]) -> int:
    arrays = sorted(nums)
    max_product = max_product_ = -math.inf
    z = arrays[0] * arrays[1]
    for i in range(2, len(arrays)):
        max_product_ = max(max_product_, z * arrays[i])

    z_ = arrays[-2] * arrays[-1]
    for i in range(len(arrays) - 3, -1, -1):
        max_product = max(max_product, z_ * arrays[i])

    return max(max_product, max_product_)


if __name__ == '__main__':
    nums_ = [1, 2, 3, 4]
    print(f'Ans: {maximum_product(nums_)}')
