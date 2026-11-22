from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dfs(x,y):
            if (x, y) == (m - 1, n - 1):
                return 1
            res = 0
            if x < m - 1:
                res += dfs(x+1,y)
            if y < n - 1:
                res += dfs(x,y+1)
            return res

        return dfs(0,0)