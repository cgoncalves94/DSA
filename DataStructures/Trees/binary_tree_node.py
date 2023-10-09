
from tree_node import TreeNode

# Define a Binary Tree Node class
class BinaryTreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

    # Method to set the left child
    def set_left(self, left_node):
        self.left = left_node

    # Method to set the right child
    def set_right(self, right_node):
        self.right = right_node

    # Method to get the left child
    def get_left(self):
        return self.left

    # Method to get the right child
    def get_right(self):
        return self.right

    # Method for In-Order Traversal (Left, Root, Right)
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    # Method for Pre-Order Traversal (Root, Left, Right)
    def pre_order_traversal(self):
        elements = [self.value]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    # Method for Post-Order Traversal (Left, Right, Root)
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.value)
        return elements
