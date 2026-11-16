from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        allCounts = defaultdict(list)
        for str in strs:
            counts = [0] * 26
            for char in str:
                counts[ord(char) - ord("a")] += 1
            allCounts[tuple(counts)].append(str)
        return list(allCounts.values())