class Stack:
    def __init__(self):
        self.items = []
    
    # Method to push a new item onto the stack
    def push(self, item):
        self.items.append(item)
    
    # Method to pop the top item off the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    # Method to peek at the top item without popping it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Method to get the stack size
    def size(self):
        return len(self.items)
