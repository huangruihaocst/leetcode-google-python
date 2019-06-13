# Solution 1: Beat 80%
class Solution:
    def findContestMatch(self, n: int) -> str:
        match = list(range(1, n + 1))
        while n > 1:
            for i in range(n >> 1):
                match[i] = '(%s,%s)' % (match[i], match[n - i - 1])
            n >>= 1
        return match[0]


# Solution 2: Beat 5%
# class Solution:
#     @staticmethod
#     def fold(l: List[int]) -> List[int]:
#         n = len(l)
#         if n == 2:
#             return l
#         res = list()
#         for i in range(n // 2):
#             res.append([l[i], l[n - i - 1]])
#         return Solution.fold(res)

#     @staticmethod
#     def to_str(l: List[int]) -> str:
#         if type(l[0]) == int:
#             return '(%d,%d)' % (l[0], l[1])
#         return '(%s,%s)' % (Solution.to_str(l[0]), Solution.to_str(l[1]))
        
#     def findContestMatch(self, n: int) -> str:
#         match = Solution.fold(list(range(1, n + 1)))
#         return Solution.to_str(match)
