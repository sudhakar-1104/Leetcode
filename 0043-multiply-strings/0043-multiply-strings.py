class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0, the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply each digit (starting from the end)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # Add to the corresponding position
                sum_ = mul + result[i + j + 1]
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        # Convert result array to string
        # Skip leading zeros
        res_str = ''.join(map(str, result)).lstrip('0')
        return res_str if res_str else "0"
