

class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class ArrayStack:

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def is_full(self):
        return len(self.stack) == self.limit

    def size(self):
        return len(self.stack)

    def contains(self, item):
        return item in self.stack
