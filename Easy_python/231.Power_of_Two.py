def is_power_of_two(n: int) -> bool:
    return True if sum(map(int, list(str(bin(n)[2:] if n > 0 else bin(n)[3:])))) == 1 else False


if __name__ == '__main__':
    print(f'Ans: {is_power_of_two(-16)}')

