def sort_colors(nums: list[int]) -> None:
    ind = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[ind], nums[i] = nums[i], nums[ind]
            ind += 1
    ind = len(nums) - 1
    start = nums.count(0)
    for i in range(start, len(nums)):
        if nums[i] == 2:
            while ind > 0 and nums[ind] == 2:
                ind -= 1
            if i > ind:
                break
            nums[i], nums[ind] = nums[ind], nums[i]


if __name__ == '__main__':
    nums_ = [2]
    print(f'Ans: {sort_colors(nums_)}')

