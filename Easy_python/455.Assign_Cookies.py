def find_content_children(g: list[int], s: list[int]) -> int:
    children = 0
    ind_g = ind_s = 0
    g.sort()
    s.sort()
    while ind_g < len(g) and ind_s < len(s):
        if g[ind_g] <= s[ind_s]:
            children += 1
            ind_g += 1
        ind_s += 1

    return children


g_ = [1, 2, 3]
s_ = [1, 3]
print(f'Ans: {find_content_children(g_, s_)}')
