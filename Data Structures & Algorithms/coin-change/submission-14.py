class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for sm in range(1, amount + 1):
            for coin in coins:
                if sm - coin >= 0:
                    dp[sm] = min(dp[sm], 1 + dp[sm - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]