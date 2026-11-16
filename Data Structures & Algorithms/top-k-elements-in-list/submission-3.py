import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        heap = []
        for num in counts:
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]