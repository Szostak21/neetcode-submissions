from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        sol = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
            