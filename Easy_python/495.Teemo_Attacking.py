def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    prev_right_border = 0
    res = 0

    for i, num in enumerate(time_series):
        res += duration - ((prev_right_border - num) if num < prev_right_border else 0)
        prev_right_border = num + duration

    return res


if __name__ == '__main__':
    timeSeries = [1, 4]
    duration_ = 2
    print(f'{find_poisoned_duration(timeSeries, duration_)}')
