# Solution 1: bucket sort
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        buckets = [None] * 2001
        for i, [x1, y1] in enumerate(workers):
            for j, [x2, y2] in enumerate(bikes):
                distance = abs(x1 - x2) + abs(y1 - y2)
                if buckets[distance] is None:
                    buckets[distance] = list()
                buckets[distance].append((i, j))

        res = [None] * len(workers)
        used = [False] * len(bikes)
        for bucket in buckets:
            if bucket is None:
                continue
            for w, b in bucket:
                if res[w] is None and not used[b]:
                    res[w] = b
                    used[b] = True

        return res

# Solution 2: Heaps in heap
# from heapq import *


# class Distance:

#     def __init__(self, b, d):
#         self.bike = b
#         self.dis = d

#     def __lt__(self, other):
#         return self.dis < other.dis or (self.dis == other.dis and self.bike < other.bike)

#     def __eq__(self, other):
#         return self.dis == other.dis and self.bike == other.bike


# class Distances:

#     def __init__(self, w):
#         self.worker = w
#         self.heap = list()
#         heapify(self.heap)

#     def __lt__(self, other):
#         return self.heap[0] < other.heap[0] or (self.heap[0] == other.heap[0] and self.worker < other.worker)

#     def push(self, dis: Distance):
#         heappush(self.heap, dis)

#     def pop(self):
#         return heappop(self.heap)

#     def peek(self):
#         return self.heap[0]


# class Solution:
#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
#         h = list()
#         heapify(h)
#         for i, [x1, y1] in enumerate(workers):
#             distances = Distances(i)
#             for j, [x2, y2] in enumerate(bikes):
#                 dis = abs(x1 - x2) + abs(y1 - y2)
#                 distances.push(Distance(j, dis))
#             heappush(h, distances)

#         taken = set()
#         d = dict()
#         while len(taken) < len(workers):
#             top_distances = heappop(h)  # type: Distances
#             if top_distances.peek().bike not in taken:  # top_distances[0] type: Distance
#                 d[top_distances.worker] = top_distances.peek().bike
#                 taken.add(top_distances.peek().bike)
#             else:
#                 top_distances.pop()
#                 heappush(h, top_distances)

#         res = list()
#         for i in range(len(workers)):
#             res.append(d[i])
#         return res
