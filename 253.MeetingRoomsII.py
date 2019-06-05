from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        end_time = list()
        heapify(end_time)
        res = 0
        for s, e in intervals:
            if len(end_time) == 0 or s < end_time[0]:
                res += 1
            else:
                heappop(end_time)
            heappush(end_time, e)
        return res

