from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        # Initially, every row can accommodate 2 groups
        # We will adjust the rows having reserved seats.
        ans = 2 * (n - len(reserved))

        for seats in reserved.values():
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # Can use both 2-5 and 6-9
                ans += 2
            elif left or middle or right:
                # Can use one block
                ans += 1
            # Otherwise, no group can be placed

        return ans