from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, high):
            if node is None:
                return True

            # Node must be strictly between low and high
            if not (low < node.val < high):
                return False

            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))