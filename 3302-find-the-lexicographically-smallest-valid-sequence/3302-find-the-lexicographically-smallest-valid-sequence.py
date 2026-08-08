from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # suf[i] = max length of suffix of word2 matchable as a subsequence
        # using word1[i:] (exact match, 0 changes allowed)
        suf = [0] * (n + 1)
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            suf[i] = m - j
        
        ans = []
        i = 0
        jj = 0
        used_change = False
        
        while i < n and jj < m:
            if word1[i] == word2[jj]:
                ans.append(i)
                i += 1
                jj += 1
            elif not used_change and suf[i + 1] >= m - jj - 1:
                used_change = True
                ans.append(i)
                i += 1
                jj += 1
            else:
                i += 1
        
        if jj == m:
            return ans
        return []