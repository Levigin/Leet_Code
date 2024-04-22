import math


def reverse(x: int) -> int:
    res = 0
    count = 10
    flag = False
    if x < 0:
        x *= -1
        flag = True
    while x:
        res += (x % 10)
        if x > 9:
            res *= count
        x //= 10
    c = pow(2, 31)
    if res < -c or res > c - 1:
        return 0
    if flag:
        return res * -1
    return res


if __name__ == '__main__':
    print(reverse(1534236469))

