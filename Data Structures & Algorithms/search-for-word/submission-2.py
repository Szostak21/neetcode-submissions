class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def dfs(r,c,i):
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if board[r][c] == word[i]:
                board[r][c] = "#"
                for dr, dc in directions:
                    if dfs(r+dr,c+dc,i+1):
                        return True
                board[r][c] = word[i]
                return False
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False