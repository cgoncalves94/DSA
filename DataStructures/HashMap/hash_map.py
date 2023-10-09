class HashMap:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.map = [None] * self.capacity
    
    # Hash function
    def _hash(self, key):
        return hash(key) % self.capacity
    
    # Rehashing function for resizing
    def _rehash(self):
        old_map = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        
        for i in old_map:
            if i is not None:
                key, value = i
                self.put(key, value)
    
    # Put a key-value pair into the map
    def put(self, key, value):
        if self.size >= self.capacity // 2:
            self._rehash()
        
        index = self._hash(key)
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = (key, value)
                return
            index = (index + 1) % self.capacity
        
        self.map[index] = (key, value)
        self.size += 1
    
    # Get a value by key
    def get(self, key):
        index = self._hash(key)
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                return self.map[index][1]
            index = (index + 1) % self.capacity
        
        return None
    
    # Remove a key-value pair by key
    def remove(self, key):
        index = self._hash(key)
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity
