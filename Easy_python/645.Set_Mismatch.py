from collections import defaultdict as d


def find_error_nums(nums: list[int]) -> list[int]:
    d_ = d(int)
    for i in range(len(nums)):
        d_[i + 1] = 0
    for i in nums:
        d_[i] += 1

    res = [0, 0]
    for key in d_:
        if d_[key] == 0:
            res[1] = key
        if d_[key] == 2:
            res[0] = key

    return res


if __name__ == '__main__':
    nums_ = [1,1,2,3,4,6,7,8,9]
    print(f'Ans: {find_error_nums(nums_)}')
