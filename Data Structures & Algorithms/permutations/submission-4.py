class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = [False] * len(nums)

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return

            for idx in range(len(nums)):
                if not used[idx]:
                    curr.append(nums[idx])
                    used[idx] = True
                    dfs(i+1)
                    curr.pop()
                    used[idx] = False

        dfs(0)
        return res