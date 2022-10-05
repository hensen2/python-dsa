class ArraySeq:
    def __init__(self):                 # O(1)
        self.array = []
        self.size = 0

    def __len__(self):                  # O(1)
        return self.size

    def __iter__(self):                 # O(n) iter_seq
        yield from self.array
