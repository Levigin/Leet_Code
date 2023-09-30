import time


class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(10 ** 3)]

    @staticmethod
    def hash_func(key: int):
        return key % 10 ** 3

    def add(self, key: int) -> None:
        val = self.hash_func(key)
        if not self.contains(key):
            self.hash_set[val] += [key]

    def remove(self, key: int) -> None:
        val = self.hash_func(key)
        for i, el in enumerate(self.hash_set[val]):
            print(f'{i = }, {el = }')
            if key == el:
                self.hash_set[val][-1], self.hash_set[val][i] = self.hash_set[val][i], self.hash_set[val][-1]
                self.hash_set[val].remove(el)

    def contains(self, key: int) -> bool:
        val = self.hash_func(key)
        return True if key in self.hash_set[val] else False


start = time.time_ns()
s = MyHashSet()
# for i in range(10 ** 6):
#     s.add(random.randint(0, 10 ** 4))
s.add(1)
s.add(2)

print(f'{s.contains(1)}')
print(f'{s.contains(3)}')
s.remove(2)
print(f'{s.contains(2)}')
finish = time.time_ns()
print(f'Time: {(finish - start) // 10 ** 6} mls')