def longestPalindrome(s: str) -> str:
    sub_str = s[0]

    def get_pal(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    for i in range(len(s) - 1):
        odd_s = get_pal(i, i)
        even_s = get_pal(i, i + 1)

        if len(odd_s) > len(sub_str):
            sub_str = odd_s
        if len(even_s) > len(sub_str):
            sub_str = even_s

    return sub_str


if __name__ == '__main__':
    print(f'{longestPalindrome("bbbb")}')
