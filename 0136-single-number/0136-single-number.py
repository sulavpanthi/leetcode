class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            a ^= nums[i]
        return a