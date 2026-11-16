from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        all_counts = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            all_counts[tuple(counts)].append(s)
        return list(all_counts.values())