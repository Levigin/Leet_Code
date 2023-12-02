class Node:
    def __init__(self, val: tuple):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'

    __repr__ = __str__


class MinStack:

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        if self.stack is None:
            new_node = Node((val, val))
        else:
            min_val = self.stack.val[1]
            if val < min_val:
                new_node = Node((val, val))
            else:
                new_node = Node((val, min_val))
            new_node.next = self.stack
        self.stack = new_node

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        if self.stack is not None:
            return self.stack.val[0]

    def getMin(self) -> int:
        return self.stack.val[1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    print(f'{stack.getMin()}')
    stack.pop()
    print(f'{stack.getMin()}')
    # print(f'{stack.top()}')

