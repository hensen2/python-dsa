"""An array implementation of the queue abstract data type that is a collection of elements with 
the following principal operations: enqueue(), dequeue(), peek_front(), peek_tail(), is_empty(), 
size(), contains(). The order in which elements come off of a queue are First In, First Out (FIFO).
"""


class QueueUnderflowError(BaseException):
    pass


class Queue:

    def __init__(self):
        self.queue = []
        self.front = 0
        self.length = 0

    def __str__(self):
        return str(self.queue)

    def enqueue(self, data):
        self.queue.append(data)
        self.length += 1

    def dequeue(self):
        if not self.queue:
            raise QueueUnderflowError
        value = self.queue[self.front]
        self.queue = self.queue[1:]
        self.length -= 1
        return value

    def is_empty(self):
        return not bool(self.queue)

    def peek_front(self):
        if not self.queue:
            raise QueueUnderflowError
        return self.queue[self.front]

    def peek_tail(self):
        if not self.queue:
            raise QueueUnderflowError
        return self.queue[-1]

    def size(self):
        return self.length

    def contains(self, item):
        return item in self.queue