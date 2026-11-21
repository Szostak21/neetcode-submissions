"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        rooms = 0

        endTimes = []

        for i in intervals:
            if not endTimes or endTimes[0] > i.start:
                rooms += 1
                heapq.heappush(endTimes,i.end)

            else:
                heapq.heappop(endTimes)
                heapq.heappush(endTimes,i.end)

        return rooms