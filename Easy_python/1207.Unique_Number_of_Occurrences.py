def unique_occurrences(arr: list[int]) -> bool:
    d = {}
    for el in arr:
        if el not in d:
            d[el] = 1
        d[el] += 1

    if len(d.values()) != len(set(d.values())):
        return False
    return True


if __name__ == '__main__':
    nums = [1, 2, 2, 1, 1, 3, 3]
    print(f'Ans: {unique_occurrences(nums)}')
