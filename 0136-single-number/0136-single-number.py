class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        num_length = len(nums)
        for i in range(num_length):
            a ^= nums[i]
        return a