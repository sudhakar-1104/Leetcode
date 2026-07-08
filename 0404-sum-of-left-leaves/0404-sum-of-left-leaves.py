class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        # Check left child
        if root.left:
            # If left child is a leaf
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Check right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total