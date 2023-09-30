def distribute_candies(candyType: list[int]) -> int:
    dif = set(candyType)
    n = len(candyType) // 2

    if len(dif) >= n:
        return n
    return len(dif)


if __name__ == '__main__':
    candyType_ = [1, 1, 2, 3]
    print(f'Ans: {distribute_candies(candyType_)}')
