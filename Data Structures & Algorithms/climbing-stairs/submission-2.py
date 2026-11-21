from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            return dfs(step+1) + dfs(step+2)

        return dfs(0)