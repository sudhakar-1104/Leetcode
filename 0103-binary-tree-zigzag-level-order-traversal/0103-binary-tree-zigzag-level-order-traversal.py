
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        result = []

        if root is None:
            return result

        queue = deque([root])
        leftToRight = True

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                node = queue.popleft()

                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
            leftToRight = not leftToRight

        return result
