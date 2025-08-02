import math
from typing import List


class Solution:
    ones_q: list[int]

    def count_bits(self, n: int) -> List[int]:
        if not Solution.ones_q:
            length = int(math.log2(10 ** 5)) + 1
            Solution.ones_q = [0] * 2 ** length
            Solution.ones_q[1] = 1
            print(f'{length = }')
            for power_of_2 in range(1, length):
                powered_2 = 2 ** power_of_2
                for i in range(powered_2, 2 * powered_2):
                    Solution.ones_q[i] = 1 + Solution.ones_q[i - powered_2]
        print(f'{Solution.ones_q = }')
        return Solution.ones_q[:n + 1]

