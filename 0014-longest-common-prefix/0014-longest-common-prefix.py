class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # # Approach 1: Using pointer
        # pointer = 0
        # min_length = min([len(s) for s in strs])
        # for _ in range(min_length):
        #     ch = strs[0][pointer]
        #     for s in strs[1:]:
        #         if not s[pointer] == ch:
        #             return strs[0][:pointer]
        #     pointer += 1
        # return strs[0][:pointer]

        
        
        # Approach 2: Using binary search approach

        def is_common_prefix(length):
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        low = 0
        high = min_length = min([len(s) for s in strs])
        while low<=high:
            mid = (low+high) // 2
            if is_common_prefix(mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low+high)//2]
            
