class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        def count_recursively(index, amount):
            if dp[index][amount] != -1:
                return dp[index][amount]
            if amount == 0:
                return 0
            if index < 0 and amount > 0:
                return float("inf")
            take = float("inf")
            if coins[index] <= amount:
                take = 1 + count_recursively(index, amount - coins[index])
            not_take = count_recursively(index - 1, amount)
            dp[index][amount] = min(take, not_take)
            return dp[index][amount]
        result = count_recursively(len(coins) - 1, amount)
        return result if result != float("inf") else -1