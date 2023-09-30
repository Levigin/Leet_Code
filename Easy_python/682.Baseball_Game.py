def cal_points(operations: list[str]) -> int:
    result = []

    for operation in operations:
        if operation.isdigit() or operation[0] == '-':
            result.append(int(operation))
        elif operation == '+':
            result.append(result[-1] + result[-2])
        elif operation == 'D':
            result.append(result[-1] * 2)
        elif operation == 'C':
            result.pop()

    return sum(result)


if __name__ == '__main__':
    ops = ["1","C"]
    print(f'Ans: {cal_points(ops)}')
