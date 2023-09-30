from collections import defaultdict as d


def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    sort_dict = d(int)
    temp = []
    for i, el in enumerate(arr1):
        if el in arr2:
            sort_dict[el] += 1
        else:
            temp.append(el)

    result = []
    temp.sort()
    for i in arr2:
        while sort_dict[i] > 0:
            result.append(i)
            sort_dict[i] -= 1

    return result + temp


if __name__ == '__main__':
    nums1 = [28,6,22,8,44,17]
    nums2 = [22,28,8,6]
    print(f'Ans: {relative_sort_array(nums1, nums2)}')
