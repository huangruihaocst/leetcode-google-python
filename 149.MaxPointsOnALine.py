# Solution 1: O(n ^ 2) time. O(n ^ 2) space.
class Solution:
    @staticmethod
    def gcd(a, b):
        return a if b == 0 else Solution.gcd(b, a % b)
    
    @staticmethod
    def cal_kb(p0, p1):
        if p0[0] == p1[0]:
            return None, p0[0]
        if p0[0] + p0[1] > p1[0] + p1[1]:
            p0, p1 = p1, p0
        g = Solution.gcd(p1[1] - p0[1], p1[0] - p0[0])
        k = ((p1[1] - p0[1]) // g, (p1[0] - p0[0]) // g)
        b = (p0[1] - k[0] * p0[0], p0[1] - k[1] * p0[0])
        return k, b
    
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n
        d = dict()
        res = 0
        for i in range(n):
            for j in range(n):
                if i < j:
                    k, b = Solution.cal_kb(points[i], points[j])
                    print(k, b)
                    if (k, b) in d:
                        d[(k, b)].add(i)
                        d[(k, b)].add(j)
                    else:
                        d[(k, b)] = {i, j}
                    res = max(res, len(d[(k, b)]))
        return res


# Solution 2: O(n ^ 2) time. O(n) space.
# class Solution:
    
#     @staticmethod
#     def gcd(a: int, b: int) -> int:
#         return a if b == 0 else Solution.gcd(b, a % b)
    
#     @staticmethod
#     def cal_k(p0: List[int], p1: List[int]) -> tuple:
#         g = Solution.gcd(p1[1] - p0[1], p1[0] - p0[0])
#         return (p1[1] - p0[1]) // g, (p1[0] - p0[0]) // g
    
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         if n <= 2:
#             return n
#         res = 1
#         for i in range(n):
#             d = dict()
#             identical = 0
#             local_max = 0
#             for j in range(i + 1, n):
#                 if i == j:
#                     continue
#                 if points[i] == points[j]:
#                     identical += 1
#                     continue
#                 if points[i][0] == points[j][0]:
#                     d[None] = d[None] + 1 if None in d else 1
#                     local_max = max(local_max, d[None])
#                 else:
#                     k = Solution.cal_k(points[i], points[j])
#                     d[k] = d[k] + 1 if k in d else 1
#                     local_max = max(local_max, d[k])
#             res = max(res, local_max + identical + 1)
#         return res
#                     