#Import Node class
from node import Node

# Define a LinkedList class
class LinkedList:
    # Initialize the LinkedList
    def __init__(self, head_node=None):
        self.head_node = head_node

    # Method to append a new node to the list
    def append(self, value):
        new_node = Node(value)  # Create a new Node object
        if not self.head_node:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.get_next_node():
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)

    # Method to delete a node by value
    def delete(self, value_to_delete):
        current_node = self.head_node
        if current_node.get_value() == value_to_delete:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node and next_node.get_value() == value_to_delete:
                    current_node.set_next_node(next_node.get_next_node())
                    break
                current_node = next_node
    
    def remove_by_value(self, value_to_remove):
        current_node = self.head_node
        
        # Special case: remove head node
        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return
        
        # General case: remove non-head node
        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = next_node

