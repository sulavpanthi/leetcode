class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, jumps = 0, 0, 0
        n = len(nums)
        while (r < n - 1):
            maxi = 0
            for i in range(l, r+1):
                maxi = max(maxi, nums[i] + i)
            jumps += 1
            l = r + 1
            r = maxi
        return jumps