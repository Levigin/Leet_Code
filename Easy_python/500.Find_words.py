def find_words(words: list[str]) -> list[str]:
    q = 'qwertyuiop'
    a = 'asdfghjkl'
    z = 'zxcvbnm'
    res = []
    for s in words:
        f = True
        if s[0].lower() in q:
            t = q
        elif s[0].lower() in a:
            t = a
        else:
            t = z
        for i in set(s):
            if i.lower() not in t:
                f = False
        if f:
            res.append(s)
    return res


if __name__ == '__main__':
    words_ = ["Hello", "Alaska", "Dad", "Peace"]
    print(f'Ans: {find_words(words_)}')
