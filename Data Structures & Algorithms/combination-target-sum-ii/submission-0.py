class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(i,rem):
            if rem == 0:
                res.append(curr.copy())
                return
            if rem < 0 or i == len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, rem - candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, rem)

        dfs(0,target)
        return res