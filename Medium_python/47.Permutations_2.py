def permute_unique(nums: list):
    result = []

    def backtracking(temp, indexes):

        if len(temp) == len(nums):
            if temp not in result:
                result.append(temp.copy())
                return

        for ind in range(len(nums)):
            if ind not in indexes:
                temp.append(nums[ind])
                indexes.append(ind)
                backtracking(temp, indexes)
                temp.pop()
                indexes.pop()

    backtracking([], [])
    return result


if __name__ == '__main__':
    arr = [1,3,2]
    print(f'Ans: {permute_unique(arr)}')
