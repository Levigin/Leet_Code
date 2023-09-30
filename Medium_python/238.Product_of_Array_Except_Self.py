def product_except(nums: list[int]) -> list[int]:
    pref_left = [1] * (len(nums) + 1)
    pref_right = [1] * (len(nums) + 1)
    zero = 0
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            zero += 1
        pref_left[i] = nums[i - 1] * pref_left[i - 1]
        pref_right[len(pref_right) - i - 1] = nums[len(nums) - i] * pref_right[len(pref_right) - i]
    print(f'{pref_left = }')
    print(f'{pref_right = }')

    if zero == 2:
        return [0] * len(nums)
    elif zero == 1:
        return [0 if nums[i - 1] != 0 else pref_left[i - 1] * pref_right[i] for i in range(1, len(nums) + 1)]

    return [pref_left[i - 1] * pref_right[i] for i in range(1, len(nums) + 1)]


nums_1 = [-1, 1, 0, -3, 3]
print(f'Ans: {product_except(nums_1)}')
