class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        rev_s = s[::-1]
        n = len(s)

        def lcs(s, rev_s):
            prev = [0 for _ in range(n+1)]
            for i in range(1, n+1):
                cur = [0 for _ in range(n+1)]
                for j in range(1, n+1):
                    if s[i-1] == rev_s[j-1]:
                        cur[j] = 1 + prev[j-1]
                    else:
                        cur[j] = max(prev[j], cur[j-1])
                prev = cur[:]
            return prev[n]

        return lcs(s, rev_s)