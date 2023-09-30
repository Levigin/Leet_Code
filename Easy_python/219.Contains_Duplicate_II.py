def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    d = {}

    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = [i]
        else:
            d[nums[i]].append(i)

    print(f'{d = }')

    arrays = list(filter(lambda x: len(x) > 1, d.values()))
    print(f'{arrays = }')

    for arr in arrays:
        for j in range(len(arr) - 1, 0, -1):
            for i in range(j):
                if arr[j] - arr[i] <= k:
                    return True

    return False


if __name__ == '__main__':
    nums_ = [1, 0, 1, 1]
    k_ = 1
    print(f'Ans: {contains_nearby_duplicate(nums_, k_)}')
