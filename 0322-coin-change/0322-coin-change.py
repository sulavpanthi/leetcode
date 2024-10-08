class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # # Approach 1: Recursion & Memoization
        # dp = [[-1]*(amount+1) for _ in range(len(coins))]
        # def count_recursively(index, amount):
        #     if dp[index][amount] != -1:
        #         return dp[index][amount]
        #     if amount == 0:
        #         return 0
        #     if index < 0 and amount > 0:
        #         return float("inf")
        #     take = float("inf")
        #     if coins[index] <= amount:
        #         take = 1 + count_recursively(index, amount - coins[index])
        #     not_take = count_recursively(index - 1, amount)
        #     dp[index][amount] = min(take, not_take)
        #     return dp[index][amount]
        # result = count_recursively(len(coins) - 1, amount)
        # return result if result != float("inf") else -1


        # Approach 2: Tabulation
        n = len(coins)
        prev = [0]*(amount+1)
        for t in range(amount+1):
            if t%coins[0] == 0:
                prev[t] = t//coins[0]
            else:
                prev[t] = float("inf")
        cur = prev
        for i in range(1, n):
            for t in range(1, amount + 1):
                not_take = 0 + prev[t]
                take = float("inf")
                if coins[i] <= t:
                    take = 1 + cur[t-coins[i]]
                cur[t] = min(take, not_take)
                prev = cur
        result = prev[amount]
        if result == float("inf"):
            return -1
        return result