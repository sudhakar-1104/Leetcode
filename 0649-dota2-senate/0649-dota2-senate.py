from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # Radiant acts first and bans Dire
                radiant.append(r + n)
            else:
                # Dire acts first and bans Radiant
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"