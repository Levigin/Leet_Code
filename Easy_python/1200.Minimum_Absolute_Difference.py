def minimum_abs_difference(arr: list[int]) -> list[list[int]]:
    result = []
    arr.sort()
    min_ = 10 ** 12
    for i in range(len(arr) - 1):
        if min_ > (c := abs(arr[i + 1] - arr[i])):
            result = [[arr[i], arr[i + 1]]]
            min_ = c
        elif min_ == abs(arr[i + 1] - arr[i]):
            result.append([arr[i], arr[i + 1]])
    return result


if __name__ == '__main__':
    nums = [1,3,6,10,15]
    print(f'Ans: {minimum_abs_difference(nums)}')
