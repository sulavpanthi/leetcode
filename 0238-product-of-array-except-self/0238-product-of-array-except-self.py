class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # First pass
        prev = nums[0]
        n = len(nums)
        res = [1 for _ in range(n)]
        for i in range(1, n):
            res[i] = prev
            prev *= nums[i]

        # second pass
        prev = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= prev
            prev *= nums[i]

        return res