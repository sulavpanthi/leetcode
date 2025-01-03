class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        def lcs(i, j):
            prev = [0 for _ in range(m+1)]
            for i in range(1, n+1):
                cur = [0 for _ in range(m+1)]
                for j in range(1, m+1):
                    if word1[i-1] == word2[j-1]:
                        cur[j] = 1 + prev[j-1]
                    else:
                        cur[j] = max(prev[j], cur[j-1])
                prev = cur[:]
            return prev[m]
        
        return n - lcs(word1, word2) + m - lcs(word1, word2)