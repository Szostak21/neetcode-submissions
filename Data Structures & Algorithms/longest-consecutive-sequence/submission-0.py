class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for num in hashSet:
            if num - 1 not in hashSet:
                length = 1
                while num + 1 in hashSet:
                    length += 1
                    num += 1
                if length > res:
                    res = length
        return res