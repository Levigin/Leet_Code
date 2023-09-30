def find_shortest_subarray(nums: list[int]) -> int:
    dict_ = {}

    for i in range(len(nums)):
        if nums[i] not in dict_:
            dict_[nums[i]] = [i, i + 1, 1]
        else:
            dict_[nums[i]][1] = i + 1
            dict_[nums[i]][2] += 1

    values = sorted(dict_.values(), key=lambda x: (-x[2], x[1] - x[0]))
    print(f'{values = }')

    return values[0][1] - values[0][0]


if __name__ == '__main__':
    n = [1, 2,3,4,5, 1]
    print(f'Ans: {find_shortest_subarray(n)}')
