from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree array
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return completed == numCourses