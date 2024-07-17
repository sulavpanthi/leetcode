class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for idx, val in enumerate(nums):
            if idx > max_index: return False
            max_index = max(idx + val, max_index)
        return True
