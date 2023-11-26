import random
import timeit

nums = [random.randint(1, 100_000_000) for _ in range(10000)]


# Time: O(n), Extra space: O(n)
def get_majority_element_1():
    check = len(nums) / 3
    majority_elements = set()
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > check:
            majority_elements.add(i)
    return majority_elements


# Time: O(n * log n), Extra space: O(1)
def get_majority_element_2():
    check = len(nums) / 3
    nums.sort()
    majority_elements_ = []
    i = 0
    j = 0
    while i < len(nums):
        while j < len(nums) and nums[i] == nums[j]:
            j += 1
        if j - i > check:
            majority_elements_.append(nums[i])
        i = j
    return majority_elements_


if __name__ == '__main__':
    # print(f'Ans: {get_majority_element(nums_)}')
    t1 = timeit.Timer("get_majority_element_1()", "from __main__ import get_majority_element_1")
    print(f'Time: {t1.timeit(100)} milliseconds')
    t2 = timeit.Timer("get_majority_element_2()", "from __main__ import get_majority_element_2")
    print(f'Time: {t2.timeit(100)} milliseconds')
