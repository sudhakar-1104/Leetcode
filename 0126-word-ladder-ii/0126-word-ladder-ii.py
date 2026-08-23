from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        # parent[word] = words that can reach 'word'
        parent = defaultdict(list)

        queue = deque([beginWord])
        visited = {beginWord}

        found = False

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new_word = word[:i] + c + word[i + 1:]

                        if new_word not in word_set:
                            continue

                        # First time seeing this word
                        if new_word not in visited:
                            if new_word not in level_visited:
                                level_visited.add(new_word)
                                queue.append(new_word)

                            parent[new_word].append(word)

                        # Another shortest path to the same word
                        elif new_word in level_visited:
                            parent[new_word].append(word)

                        if new_word == endWord:
                            found = True

            visited.update(level_visited)

        if endWord not in parent:
            return []

        # Reconstruct paths using DFS
        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for prev in parent[word]:
                path.append(prev)
                dfs(prev)
                path.pop()

        dfs(endWord)

        return result