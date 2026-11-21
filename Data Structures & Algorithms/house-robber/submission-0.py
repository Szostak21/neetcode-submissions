from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i):
            if i > len(nums) - 1:
                return 0
            elif i == len(nums) - 1:
                return nums[i]
            return max(nums[i] + dfs(i+2), dfs(i+1))

        return dfs(0)