class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        ans = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            # If current index reaches the partition end
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans