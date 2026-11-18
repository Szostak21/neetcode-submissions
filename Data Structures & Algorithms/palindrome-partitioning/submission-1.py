class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(i,j):
            sub = s[i:j]
            if j == len(s):
                if sub == sub[::-1]:
                    curr.append(sub)
                    res.append(curr.copy())
                    curr.pop()
                return

            if sub == sub[::-1]:
                curr.append(sub)
                dfs(j,j+1)
                curr.pop()
            dfs(i,j+1)

        dfs(0,1)
        return res