class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        el = self.q[-1]
        self.q = self.q[:-1]
        return el

    def top(self):
        if not self.empty():
            return self.q[-1]
        return None

    def empty(self) -> bool:
        if self.q:
            return False
        return True

    def __str__(self):
        return f'{self.q}'

    def __repr__(self):
        return f'{str(self)}'


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(f'{param_2 = }, {param_3 = }, {param_4 = }')
