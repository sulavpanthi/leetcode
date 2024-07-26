class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        # sliding window approach, p1 to expand, p2 to contract
        p1, p2 = 0, 0
        n = len(s)
        result = 0
        visited = set()
        
        while p1 < n and p2 < n:

            if s[p1] not in visited:
                visited.add(s[p1])
                p1 += 1
                result = max(result, p1-p2)
            else:
                visited.remove(s[p2])
                p2 += 1
        
        return result