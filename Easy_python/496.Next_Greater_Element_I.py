def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for i in nums1:
        ind = nums2.index(i)
        while ind < len(nums2) and nums2[ind] <= i:
            ind += 1
        if ind == len(nums2):
            result.append(-1)
        else:
            result.append(nums2[ind])
    return result


if __name__ == '__main__':
    nums1_ = [5, 3, 6]
    nums2_ = [3, 4, 5, 6]
    print(f'Ans: {next_greater_element(nums1_, nums2_)}')
