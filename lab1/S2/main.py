class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack is None or val <= self.min_stack:
            self.min_stack = val

    def pop(self) -> None:
        if self.stack:
            poped = self.stack[-1]
            self.stack.pop()
            if poped == self.min_stack:
                self.min_stack = self.__findMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack
    
    def __findMin(self):
        if len(self.stack) == 0:
            return None
        min = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < min:
                min = self.stack[i]
        return min
