def find_special_integer(arr: list[int]) -> int:
    for i in set(arr):
        if arr.count(i) / len(arr) * 100 > 25:
            return i


if __name__ == '__main__':
    nums = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(f'Ans: {find_special_integer(nums)}')
