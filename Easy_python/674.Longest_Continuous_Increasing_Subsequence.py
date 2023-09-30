def find_length_of_lcis(nums: list[int]) -> int:
    counter = 1
    max_length = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            counter += 1
        else:
            counter = 1
        max_length = max(max_length, counter)

    return max_length


if __name__ == '__main__':
    nums_ = [11]
    print(f'Ans: {find_length_of_lcis(nums_)}')
