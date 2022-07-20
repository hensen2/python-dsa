class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, data):
        pass