class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        res = []
        curr = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(curr))
                return
            
            for char in digit_to_char[digits[i]]:
                curr.append(char)
                dfs(i+1)
                curr.pop()

        dfs(0)
        return res