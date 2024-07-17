class Solution:


    def checkValidString(self, s: str) -> bool:
        
        # # Approach 1: Using simple recursion and memoization
        # dp = [[0] * len(s) for i in range(len(s))]
        # def check_recursively(s, index, count):
        #     if index == len(s):
        #         return count == 0
        #     if count < 0:
        #         return False
        #     if dp[index][count] != 0: return dp[index][count]
        #     if s[index] == '(':
        #         dp[index][count] = check_recursively(s, index + 1, count + 1)
        #     elif s[index] == ')':
        #         dp[index][count] = check_recursively(s, index + 1, count - 1)
        #     else:
        #         dp[index][count] = check_recursively(s, index + 1, count) or check_recursively(s, index + 1, count + 1) or check_recursively(s, index + 1, count - 1)
        #     return dp[index][count]
        # return check_recursively(s, index = 0, count = 0)

        # Approach 2: Using greedy approach
        low = 0
        high = 0
        for i in range(len(s)):
            if s[i] == '(':
                low += 1
                high += 1
            elif s[i] == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if low < 0: low = 0
            if high < 0: return False
        return low == 0