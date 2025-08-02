from typing import List


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def rec(i, temp_, sum_, result_):

        if sum_ > target:
            return

        if sum(temp_) == target:
            result_.append(temp_.copy())
            return

        for ind in range(i, len(candidates)):
            if ind > i and candidates[ind] == candidates[ind - 1]:
                continue
            sum_ += candidates[ind]
            temp_.append(candidates[ind])
            rec(ind + 1, temp_, sum_, result_)
            sum_ -= candidates[ind]
            temp_.pop()

    candidates.sort()
    rec(0, [], 0, result)

    return result


if __name__ == "__main__":
    nums = [2, 5, 2, 1, 2]
    t = 5
    print(f'Ans: {combination_sum_2(nums, t)}')
