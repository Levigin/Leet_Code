def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams_dict = {}

    for val in strs:
        if ''.join(sorted(val)) not in anagrams_dict:
            anagrams_dict[''.join(sorted(val))] = [val]
        else:
            anagrams_dict[''.join(sorted(val))].append(val)
    return list(anagrams_dict.values())


if __name__ == '__main__':
    nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f'Ans: {group_anagrams(nums)}')
