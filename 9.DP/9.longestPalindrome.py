class Solution3:
    def lcs(self, s):
        text1 = s
        text2 = s[::-1]
        n = len(text1)
        m = len(text2)
        
        # Initialize dp table with size (n+1) x (m+1) and all values 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # Fill dp table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]



sol = Solution3()
print(sol.lcs("bbbab"))  # Output: 4 → "bbbb"
