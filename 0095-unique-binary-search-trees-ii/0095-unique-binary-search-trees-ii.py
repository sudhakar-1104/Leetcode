class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def build(start, end):
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            trees = []

            for root in range(start, end + 1):
                leftTrees = build(start, root - 1)
                rightTrees = build(root + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            memo[(start, end)] = trees
            return trees

        return build(1, n)