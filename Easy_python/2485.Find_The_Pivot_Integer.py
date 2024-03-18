from math import floor, sqrt


class Solution:

    @staticmethod
    def pivotInteger(n: int) -> int:
        total = (n * (n + 1)) // 2
        m = floor(sqrt(total))
        if m * m == total:
            return int(m)
        return -1


if __name__ == '__main__':
    print(f'{Solution.pivotInteger(8)}')
