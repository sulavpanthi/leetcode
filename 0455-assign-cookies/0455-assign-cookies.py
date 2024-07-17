class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_pointer, s_pointer = 0, 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                g_pointer += 1
            s_pointer += 1
        return g_pointer