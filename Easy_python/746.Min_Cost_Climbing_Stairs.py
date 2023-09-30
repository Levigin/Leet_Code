def min_cost_climbing_stairs(cost: list[int]) -> int:
    dp = [0] * len(cost)
    for i in range(len(cost)):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[-1], dp[-2])


if __name__ == '__main__':
    n = [10, 15, 20]
    nums = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f'Ans: {min_cost_climbing_stairs(nums)}')
