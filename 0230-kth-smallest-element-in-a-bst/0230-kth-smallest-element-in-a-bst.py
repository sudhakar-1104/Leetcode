class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while True:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the smallest unvisited node
            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            # Move to the right subtree
            current = current.right