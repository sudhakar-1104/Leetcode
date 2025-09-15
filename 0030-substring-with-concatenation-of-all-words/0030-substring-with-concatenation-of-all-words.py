from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            count = 0
            current_counts = defaultdict(int)

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_counts:
                    current_counts[word] += 1
                    
                    if current_counts[word] <= word_counts[word]:
                        count += 1
                    
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        if current_counts[left_word] < word_counts[left_word]:
                            count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    current_counts.clear()
                    count = 0
                    left = j + word_len

        return result