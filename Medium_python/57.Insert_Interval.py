def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result_intervals = []
    left = 0
    right = len(intervals)

    # Binary search
    left_ind = binary_search(intervals, new_interval[0], left, right)
    right_ind = binary_search(intervals, new_interval[1], left, right)
    print(f'left: {left_ind}, right: {right_ind}')

    # Index
    i = 0
    if right_ind < i and left_ind < i:
        result_intervals.append(new_interval)
    while i < len(intervals):
        if i < left_ind or i > right_ind:
            result_intervals.append(intervals[i])
        else:
            if intervals[left_ind][0] < new_interval[0] <= intervals[left_ind][1]:
                l_ = intervals[left_ind][0]
            elif new_interval[0] > intervals[left_ind][1]:
                result_intervals.append(intervals[left_ind])
                l_ = new_interval[0]
            else:
                l_ = new_interval[0]

            while i != right_ind:
                i += 1

            if intervals[right_ind][0] <= new_interval[1] < intervals[right_ind][1]:
                r_ = intervals[right_ind][1]
            else:
                r_ = new_interval[1]

            result_intervals.append([l_, r_])
        i += 1

    return result_intervals


def binary_search(intervals: list[list[int]], key: int, left: int, right: int):
    if left >= right:
        return left - 1

    pivot = (right + left) // 2

    if intervals[pivot][0] < key:
        return binary_search(intervals, key, pivot + 1, right)
    elif intervals[pivot][0] > key:
        return binary_search(intervals, key, left, pivot)
    else:
        return pivot


if __name__ == '__main__':
    intervals_ = [[1, 5], [10, 15]]
    new_intervals_ = [6, 9]
    print(f'Search: {insert(intervals_, new_intervals_)}')
