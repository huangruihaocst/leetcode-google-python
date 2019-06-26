from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dd = defaultdict(lambda: 0)
        for num, start, end in trips:
            dd[start] += num
            dd[end] -= num
        curr = 0
        for stop in sorted(dd.keys()):
            curr += dd[stop]
            if curr > capacity:
                return False
        return True

