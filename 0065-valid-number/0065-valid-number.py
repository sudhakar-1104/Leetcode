class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        i = 0

        # Optional sign
        if i < n and s[i] in "+-":
            i += 1

        # Digits before decimal point
        digits_before = 0
        while i < n and s[i].isdigit():
            i += 1
            digits_before += 1

        # Optional decimal point
        digits_after = 0
        if i < n and s[i] == '.':
            i += 1

            while i < n and s[i].isdigit():
                i += 1
                digits_after += 1

        # Must have at least one digit
        # either before or after the decimal point
        if digits_before == 0 and digits_after == 0:
            return False

        # Optional exponent
        if i < n and s[i] in "eE":
            i += 1

            # Optional exponent sign
            if i < n and s[i] in "+-":
                i += 1

            # Exponent must contain at least one digit
            exponent_digits = 0
            while i < n and s[i].isdigit():
                i += 1
                exponent_digits += 1

            if exponent_digits == 0:
                return False

        # Everything must have been consumed
        return i == n