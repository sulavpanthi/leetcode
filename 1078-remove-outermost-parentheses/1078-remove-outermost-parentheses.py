class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count = 0
        closed_count = 0
        start = 0
        res = ""
        for i, c in enumerate(s):
            if c == '(':
                open_count += 1
            elif c == ')':
                closed_count += 1
            if open_count == closed_count:
                res += s[start+1:i]
                start = i + 1
        return res