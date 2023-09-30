def is_anagram(s: str, t: str) -> bool:
    d1 = {}
    d2 = {}

    for i in s:
        if i not in d1:
            d1[i] = 0
        else:
            d1[i] += 1

    for i in t:
        if i not in d1:
            d2[i] = 0
        else:
            d2[i] += 1

    return d1 == d2


s_ = ""
t_ = ""

print(f'ans: {is_anagram(s_, t_)}')
