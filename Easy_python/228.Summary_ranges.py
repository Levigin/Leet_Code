def summary_ranges(nums: list[int]) -> list[str]:
    lp = 0
    rp = 0
    res = []
    while lp < len(nums):
        while rp < len(nums) - 1 and nums[rp + 1] - nums[rp] == 1:
            rp += 1
        res.append(f"{nums[lp]}->{nums[rp]}" if lp != rp else f"{nums[lp]}")
        lp = rp + 1
        rp = lp

    return res


if __name__ == '__main__':
    nums_ = [0, 2, 3, 4, 6, 8, 9]
    print(f'Ans: {summary_ranges(nums_)}')
