class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(opened,closed):
            if opened == n:
                for _ in range(n-closed):
                    curr.append(")")
                res.append("".join(curr))
                for _ in range(n-closed):
                    curr.pop()
                return
            
            curr.append("(")
            dfs(opened+1,closed)
            curr.pop()

            if opened > closed:
                curr.append(")")
                dfs(opened,closed+1)
                curr.pop()
            
        dfs(0,0)
        return res