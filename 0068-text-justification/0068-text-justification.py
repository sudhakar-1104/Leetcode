
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        result = []
        i = 0

        while i < len(words):

            j = i
            total_chars = 0

            # Step 1: Find maximum words that fit in this line
            while j < len(words) and total_chars + len(words[j]) + (j - i) <= maxWidth:
                total_chars += len(words[j])
                j += 1

            num_words = j - i
            spaces = maxWidth - total_chars

            # Step 2: Last line OR line with only one word
            if j == len(words) or num_words == 1:

                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                # Step 3: Distribute spaces evenly
                gaps = num_words - 1

                space_between = spaces // gaps
                extra_spaces = spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]

                    # Left gaps get extra spaces
                    if k - i < extra_spaces:
                        line += " " * (space_between + 1)
                    else:
                        line += " " * space_between

                line += words[j - 1]

            result.append(line)

            # Move to the next line
            i = j

        return result
