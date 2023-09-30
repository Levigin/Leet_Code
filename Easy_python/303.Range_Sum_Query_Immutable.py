class NumArray:

    def __init__(self, nums: list[int]):
        # При инициализации времени тратится меньше чем при вызове и обработке
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


if __name__ == '__main__':
    nums_ = [-2, 0, 3, -5, 2, -1]
    num = NumArray(nums_)
    print(f'Ans: {num.sumRange(0, 5)}')
