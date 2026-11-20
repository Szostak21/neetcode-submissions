import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(maxHeap, -y)

        return -maxHeap[0] if maxHeap else 0