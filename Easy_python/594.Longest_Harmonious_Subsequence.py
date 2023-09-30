from collections import defaultdict as d


def find_lhs(nums: list[int]) -> int:
    d_ = d(int)

    for i in nums:
        d_[i] += 1

    list_keys = sorted(d_.keys(), key=lambda x: x)
    max_length = 0
    for i, key in enumerate(list_keys[:-1]):
        if (k1 := list_keys[i + 1]) - key == 1:
            max_length = max(max_length, d_[k1] + d_[key])

    return max_length


if __name__ == '__main__':
    nums_ = [1, 3, 2, 2, 5, 2, 3, 7]  # 1 2 2 2 3 3 5 7
    print(f'Ans: {find_lhs(nums_)}')
