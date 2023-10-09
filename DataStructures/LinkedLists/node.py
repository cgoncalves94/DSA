# Define a Node class compatible with Doubly LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None  # Pointer to the previous node, default is None
        self.next = None  # Pointer to the next node, default is None

    # Method to set the next node
    def set_next_node(self, next_node):
        self.next = next_node

    # Method to get the next node
    def get_next_node(self):
        return self.link_node
    
    # Method to set the previous node
    def set_prev_node(self, prev_node):
        self.prev = prev_node
        
    # Method to get the previous node
    def get_prev_node(self):
        return self.prev

    # Method to get the node value
    def get_value(self):
        return self.value
