class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for each in nums:
            a ^= each
        return a