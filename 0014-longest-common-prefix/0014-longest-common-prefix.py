class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        min_length = min([len(s) for s in strs])
        for _ in range(min_length):
            ch = strs[0][pointer]
            for s in strs[1:]:
                if not s[pointer] == ch:
                    return strs[0][:pointer]
            pointer += 1
        return strs[0][:pointer]
