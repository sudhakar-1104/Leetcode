from collections import Counter
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        hand = Counter(hand)

        # Remove all consecutive groups of length >= 3
        def shrink(s):
            changed = True
            while changed:
                changed = False
                i = 0
                new = ""
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        new += s[i:j]
                    i = j
                s = new
            return s

        @lru_cache(None)
        def dfs(cur_board, hand_state):
            if not cur_board:
                return 0

            cnt = Counter()
            for c, k in zip("RYBGW", hand_state):
                cnt[c] = k

            ans = float("inf")

            for i in range(len(cur_board) + 1):
                for color in "RYBGW":
                    if cnt[color] == 0:
                        continue

                    # Skip useless insertions
                    if i > 0 and cur_board[i - 1] == color:
                        continue
                    if (i < len(cur_board) and cur_board[i] == color) or (
                        i > 0
                        and i < len(cur_board)
                        and cur_board[i - 1] == cur_board[i] != color
                    ):
                        cnt[color] -= 1

                        nxt = shrink(cur_board[:i] + color + cur_board[i:])

                        nxt_state = tuple(cnt[c] for c in "RYBGW")

                        res = dfs(nxt, nxt_state)

                        if res != float("inf"):
                            ans = min(ans, res + 1)

                        cnt[color] += 1

            return ans

        start = tuple(hand[c] for c in "RYBGW")
        ans = dfs(board, start)

        return -1 if ans == float("inf") else ans