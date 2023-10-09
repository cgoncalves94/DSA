from binary_tree_node import BinaryTreeNode

# Define a Binary Search Tree Node class
class BinarySearchTree(BinaryTreeNode):
    # Method to add a value to the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    # Method to search for a value in the tree
    def search(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)
        return False

    # Method to find the minimum value node
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.value

    # Method to find the maximum value node
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.value

    # Delete a value from the tree
    def delete(self, value):
        # Start the deletion recursion at the root
        self.root = self._delete_recursive(self.root, value)
    # Recursively delete the given value starting from the given node
    def _delete_recursive(self, node, value):
        # Base case - node to delete is not found
        if node is None:
            return node
        # Value is less than node's value - recurse down left subtree    
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        # Value is greater than node's value - recurse down right subtree
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        # Value is equal to node's value - delete this node
        else:
            # Node has no left child - return right subtree as new node     
            if node.left is None:
                return node.right
            # Node has no right child - return left subtree as new node
            elif node.right is None:
                return node.left
            # Node has two children -  
            # Find minimum value in right subtree as successor
            # Set node's value to successor value
            # Recursively delete successor value        
            else:
                successor = self._find_min_value(node.right)
                node.value = successor
                node.right = self._delete_recursive(node.right, successor)
        # Return the updated node after any recursive calls to children
        return node
