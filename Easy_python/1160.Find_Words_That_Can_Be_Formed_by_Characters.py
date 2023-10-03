from collections import defaultdict as d


def count_characters(words: list[str], chars: str) -> int:
    d_chars = d(int)
    for i in chars:
        d_chars[i] += 1

    res = 0
    for word in words:
        flag = False
        temp = d_chars.copy()
        for ch in word:
            if ch not in temp:
                flag = True
                break
            else:
                temp[ch] -= 1
                if temp[ch] < 0:
                    flag = True
                    break
        if not flag:
            res += len(word)

    return res


if __name__ == '__main__':
    nums = ["cat", "bt", "hat", "tree"]
    target = "atach"
    print(f'Ans: {count_characters(nums, target)}')
