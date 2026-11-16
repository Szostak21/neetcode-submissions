class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
    
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            start = i + 1
            end = start + length
            res.append(s[start:end])
            i ,j = end, end
        return res
            