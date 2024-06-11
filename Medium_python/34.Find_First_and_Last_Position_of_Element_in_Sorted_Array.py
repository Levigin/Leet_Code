def search_range(nums: list, target: int):
    left, right = 0, len(nums) - 1
    mid = -1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            break
    print(left, right)

    if mid != -1 and left < right:
        while nums[left] != target:
            left += 1
        while nums[right] != target:
            right -= 1
    else:
        return [-1, -1]

    return [left, right]


if __name__ == '__main__':
    nums_ = [5,7,7,8,8,10]
    t = 6
    print(f'{search_range(nums_, t)}')
