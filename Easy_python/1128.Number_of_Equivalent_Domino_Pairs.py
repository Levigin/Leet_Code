def num_equiv_domino_pairs(dominoes: list[list[int]]) -> int:
    counter = 0
    d = {}

    for i, j in dominoes:
        if (i, j) in d or (j, i) in d:
            key = d.get((i, j), 0)
            if key != 0:
                d[(i, j)] += 1
            else:
                d[(j, i)] += 1
        else:
            d[(i, j)] = 1

    for key in d:
        if (c := d[key]) != 1:
            counter += (c * (c - 1)) // 2

    return counter


if __name__ == '__main__':
    nums = [[1,2],[2,1],[3,4],[5,6]]
    print(f'Ans: {num_equiv_domino_pairs(nums)}')
