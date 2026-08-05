from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check whether any outside node invokes a suspicious node
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans