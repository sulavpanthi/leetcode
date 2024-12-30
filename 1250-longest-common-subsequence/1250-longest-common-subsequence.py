class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        def lcs(i, j):
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + lcs(i-1, j-1)
            else:
                dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))
            return dp[i][j]
        return lcs(len(text1) - 1, len(text2) - 1)