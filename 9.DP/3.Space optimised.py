# Space 


class Solution:
    def fibo(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1  # Represents dp[i-2] and dp[i-1]
        for _ in range(2, n + 1):
            a, b = b, a + b  # b becomes dp[i], a becomes dp[i-1]

        return b
