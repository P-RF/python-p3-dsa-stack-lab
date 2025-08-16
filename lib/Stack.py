class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.items: # if the stack is not empty, pop item
            return self.items.pop()
        else:
            return None # return None if stack is empty

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        distance = 0
        for item in reversed(self.items):
            if item == target:
                return distance
            distance += 1
        return -1
