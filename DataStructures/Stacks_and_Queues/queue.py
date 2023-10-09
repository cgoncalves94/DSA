class Queue:
    def __init__(self):
        self.items = []
    
    # Method to enqueue a new item into the queue
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # Method to dequeue the front item from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    # Method to check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Method to get the queue size
    def size(self):
        return len(self.items)
