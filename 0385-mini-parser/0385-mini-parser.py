class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # If the input is just a single integer
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        
        for ch in s:
            if ch == '[':
                # Start a new nested list
                stack.append(NestedInteger())

            elif ch == '-' or ch.isdigit():
                # Build the current number
                num += ch

            elif ch == ',' or ch == ']':
                # If a number was being built, add it
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

                if ch == ']':
                    # Completed the current list
                    completed = stack.pop()

                    if not stack:
                        return completed

                    # Add completed list to its parent
                    stack[-1].add(completed)