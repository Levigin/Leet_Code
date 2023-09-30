def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    f = [0] + flowerbed
    f.append(0)
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        n -= 1

    for i in range(1, len(f) - 1):
        if f[i - 1] != 1 and f[i] != 1 and f[i + 1] != 1:
            f[i] = 1
            n -= 1
    print(f'{f = }')
    if n <= 0:
        return True
    return False


if __name__ == '__main__':
    flowerbed_ = [0, 0, 0]
    n_ = 2
    print(f'Ans: {can_place_flowers(flowerbed_, n_)}')
