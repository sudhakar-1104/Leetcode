class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        current = 0
        for change in diff:
            current += change
            if current > capacity:
                return False

        return True