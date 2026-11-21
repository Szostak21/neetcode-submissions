from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(i):
            if i < 0:
                return float('inf')
            if i == 0:
                return 0
            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, 1 + dfs(i - coin))
            return minCoins
        res = dfs(amount)
        return res if res != float('inf') else -1

            