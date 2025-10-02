class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # Helper function for recursion
        def inorder(node, res):
            if node:
                inorder(node.left, res)   # Traverse left subtree
                res.append(node.val)      # Visit node
                inorder(node.right, res)  # Traverse right subtree
        result = []
        inorder(root, result)
        return result