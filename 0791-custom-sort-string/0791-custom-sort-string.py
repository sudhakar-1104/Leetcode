from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        ans = []

        for ch in order:
            if ch in freq:
                ans.append(ch * freq[ch])
                del freq[ch]

        for ch, cnt in freq.items():
            ans.append(ch * cnt)

        return "".join(ans)