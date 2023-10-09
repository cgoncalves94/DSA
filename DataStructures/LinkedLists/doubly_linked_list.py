#Import Node class
from node import Node


# Define a DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method to add a node at the beginning of the list
    def add_to_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Method to add a node at the end of the list
    def add_to_tail(self, value):
        new_node = Node(value)  # Create a new Node object
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Method to remove a node from the beginning of the list
    def remove_from_head(self):
        if self.head is None:
            return None
        removed_node = self.head
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next
        return removed_node.value

    # Method to remove a node from the end of the list
    def remove_from_tail(self):
        if self.tail is None:
            return None
        removed_node = self.tail
        if self.tail.prev:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        return removed_node.value

    def remove_by_value(self, value_to_remove):
        current_node = self.head
        
        # Special case: remove head node
        if current_node and current_node.get_value() == value_to_remove:
            self.head = current_node.get_next_node()
            if self.head:
                self.head.set_prev_node(None)
            return
        
        # General case: remove non-head node
        while current_node:
            if current_node.get_value() == value_to_remove:
                prev_node = current_node.get_prev_node()
                next_node = current_node.get_next_node()
                
                if prev_node:
                    prev_node.set_next_node(next_node)
                if next_node:
                    next_node.set_prev_node(prev_node)
                    
                return
            current_node = current_node.get_next_node()
