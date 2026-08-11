class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        # Convert k to 0-based index
        k -= 1

        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)

            index = k // fact
            k %= fact

            result.append(numbers[index])
            numbers.pop(index)

        return "".join(result)