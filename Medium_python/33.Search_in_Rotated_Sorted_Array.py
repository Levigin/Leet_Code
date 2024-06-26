def search(nums: list[int], target: int) -> int:

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        print(f'mid: {mid}')

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    nums_ = [5, 1, 3]
    t = 3
    print(f'{search(nums_, t)}')
