from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            tank += diff

            # Current starting point cannot reach station i + 1
            if tank < 0:
                start = i + 1
                tank = 0

        # Not enough gas overall
        if total < 0:
            return -1

        return start