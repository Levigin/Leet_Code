def next_greatest_letter(letters: list[str], target: str) -> str:
    i = 0
    while i < len(letters):
        if letters[i] > target and i == 0:
            return letters[0]
        elif letters[i] == target:
            while i < len(letters) and letters[i] == target:
                i += 1
            if i == len(letters):
                return letters[0]
            else:
                return letters[i]
        elif i < len(letters) and letters[i] > target:
            return letters[i]
        else:
            i += 1
    return letters[0]


if __name__ == '__main__':
    let = ["c", "f", "j"]
    t = 'g'
    print(f'Ans: {next_greatest_letter(let, t)}')
