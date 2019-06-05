# Solution 1: O(n ^ 2)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        visited = set()
        for x0, y0 in points:
            for x1, y1 in visited:
                if (x0, y1) in visited and (x1, y0) in visited:
                    area = abs(x1 - x0) * abs(y1 - y0)
                    if area and area < res:
                        res = area
            visited.add((x0, y0))
        return res if res < float('inf') else 0

# Solution 2: O(n ^ 1.5)
# class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
#         n = len(points)
#         x_cnt = len(set(x for x, y in points))
#         y_cnt = len(set(y for x, y in points))
#         if x_cnt == n or y_cnt == n:
#             return 0
        
#         d = dict()
#         if x_cnt > y_cnt:
#             for x, y in points:
#                 if x in d:
#                     d[x].append(y)
#                 else:
#                     d[x] = [y]
#         else:
#             for x, y in points:
#                 if y in d:
#                     d[y].append(x)
#                 else:
#                     d[y] = [x]
        
#         last_x = dict()
#         res = float('inf')
#         for x in sorted(d):
#             d[x].sort()
#             for i in range(len(d[x])):
#                 for j in range(i):
#                     # j < i
#                     y0, y1 = d[x][j], d[x][i]
#                     if (y0, y1) in last_x:
#                         res = min(res, (y1 - y0) * (x - last_x[(y0, y1)]))
#                     last_x[(y0, y1)] = x
#         return res if res < float('inf') else 0
#                 