def find_restaurant(list1: list[str], list2: list[str]) -> list[str]:
    res = []
    min_v = len(list1) + len(list2)
    for i, s in enumerate(list1):
        if s in list2:
            val = list2.index(s)
            min_v = min(min_v, val + i)
            res.append([s, val + i])

    res = filter(lambda x: x[1] == min_v, res)

    return [i[0] for i in res]


if __name__ == '__main__':
    l1 = ["happy", "sad", "good"]
    l2 = ["sad", "happy", "good"]
    print(f'Ans: {find_restaurant(l1, l2)}')
