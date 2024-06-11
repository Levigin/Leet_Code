def my_atoi(s: str):
    new_s = ""
    flag = True
    word = 0
    while word < len(s) and (
            s[word].isdigit() or (s[word] == "-" and flag and len(new_s) == 0) or (s[word] == ' ' and len(new_s) == 0) or (
            s[word] == '+' and flag and len(new_s) == 0)):
        if s[word] == ' ':
            word += 1
            continue
        new_s += s[word]
        word += 1

    if len(new_s) == 0 or new_s == "+" or new_s == '-':
        return 0
    print(f'{new_s}')
    new_s = int(new_s)
    if int(new_s) < -(2 ** 31) or int(new_s) > (2 ** 31) - 1:
        if int(new_s) < 0:
            return -2 ** 31
        else:
            return 2 ** 31 - 1

    return new_s


if __name__ == '__main__':
    print(f'{my_atoi("+-12")}')
