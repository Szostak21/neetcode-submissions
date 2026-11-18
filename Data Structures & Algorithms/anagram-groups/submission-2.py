from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        AllCounts = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            AllCounts[tuple(count)].append(s)

        res = []
        for words in AllCounts.values():
            res.append(words)

        return res