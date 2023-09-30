def decode(encoded, first):
    new_nums = [0 * i for i in range(len(encoded) + 1)]
    new_nums[0] = first
    i = 0
    count = 1
    while i < len(encoded):
        new_nums[count] = new_nums[i] ^ encoded[i]
        i += 1
        count += 1

    return new_nums


print(decode([1, 2, 3], 1))
