def four_sum(nums: list[int], target) -> list[list[int]]:
    nums.sort()
    if len(nums) < 4:
        return []
    a, b, c, d = 0, 1, len(nums) - 2, len(nums) - 1
    result = []
    while a < len(nums) - 3:
        while a + 1 < d - 1:
            first_pair = nums[a] + nums[d]
            while b < c:
                second_pair = nums[b] + nums[c]
                if first_pair + second_pair == target:
                    if (s := [nums[a], nums[b], nums[c], nums[d]]) not in result:
                        result.append(s)
                    b += 1
                    c -= 1
                elif target - first_pair < second_pair:
                    c -= 1
                elif target - first_pair > second_pair:
                    b += 1

            d -= 1
            b = a + 1
            c = d - 1

        a += 1
        d = len(nums) - 1
        b = a + 1
        c = d - 1

    return result


if __name__ == '__main__':
    arr = [-2, -1, 3, -3, 4, 0, 0, 1, 2]
    arr1 = [2, 2, 2, 2, 2]
    t = 8
    print(f'Ans: {four_sum(arr1, t)}')
