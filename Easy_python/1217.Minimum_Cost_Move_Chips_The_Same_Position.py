def min_cost_to_move_chips(position: list[int]) -> int:
    even_q = 0
    odd_q = 0
    for i in position:
        if i % 2 == 0:
            even_q += 1
        else:
            odd_q += 1

    return min(even_q, odd_q)


if __name__ == '__main__':
    nums = [1, 10000000000]
    print(f'Ans: {min_cost_to_move_chips(nums)}')
