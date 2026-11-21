from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(n):
            @cache
            def dfs(i):
                if i >= len(n):
                    return 0
                return max(n[i] + dfs(i+2), dfs(i+1))
            return dfs(0)

        return max(helper(nums[:-1]), helper(nums[1:]))
        