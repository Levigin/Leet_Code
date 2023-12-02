class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_ = []
        self.counter = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stack_.append(self.counter)
        self.counter -= 1

    def pop(self) -> int:
        ind = self.stack_.pop()
        self.counter += 1
        return self.stack[ind]

    def peek(self) -> int:
        ind = self.stack_[-1]
        return self.stack[ind]

    def empty(self) -> bool:
        return False if self.stack_ else True


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    q.push(5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())