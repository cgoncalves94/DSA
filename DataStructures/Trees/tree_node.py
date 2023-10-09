
# Define a Tree Node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    # Method to add a child
    def add_child(self, child_node):
        self.children.append(child_node)
        
    # Method to remove a child
    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]
        
    # Method to traverse the tree
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print("Visited:", current_node.value)
            nodes_to_visit += current_node.children[::-1]
