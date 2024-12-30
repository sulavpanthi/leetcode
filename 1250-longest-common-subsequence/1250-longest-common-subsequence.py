class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # # Approach 1: Memoization
        # n, m = len(text1), len(text2)
        # dp = [[-1 for j in range(m)] for i in range(n)]
        # def lcs(i, j):
        #     if i<0 or j<0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if text1[i] == text2[j]:
        #         dp[i][j] = 1 + lcs(i-1, j-1)
        #     else:
        #         dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))
        #     return dp[i][j]
        # return lcs(len(text1) - 1, len(text2) - 1)

        # Approach 2: Tabulation
        n, m = len(text1), len(text2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
