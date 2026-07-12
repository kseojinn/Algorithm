class Stack:
    def __init__(self):
        self.data = []

    def load(self, items):
        for item in items:
            self.push(item)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
    
stack = Stack()

# Insert data.
stack.load([])

while not stack.is_empty():
    print(stack.pop())