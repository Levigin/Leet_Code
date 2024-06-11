def convert(s: str, num_rows: int) -> str:
    conv = ["" for _ in range(num_rows)]
    i = 0
    count = 0
    if num_rows == 1:
        return s
    while i < len(s):

        while i < len(s) and count < num_rows:
            print(f'1. count: {count}, i: {i}')
            conv[count] += s[i]
            count += 1
            i += 1

        count -= 2

        while i < len(s) and count > -1:
            print(f'2. count: {count}, i: {i}')
            conv[count] += s[i]
            count -= 1
            i += 1

        count += 2

    print(f'conv: {conv}')
    res = ""
    for i in conv:
        res += i
    return res


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 1))