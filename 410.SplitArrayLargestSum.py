# Solution 1: Greedy + Binary Search
# AC
class Solution:
    @staticmethod
    def smaller(nums: List[int], limit: int, m: int) -> bool:
        current, cnt = 0, 1
        res = True
        for i in nums:
            if i > limit:
                res = False
                break
            if current + i > limit:
                current = i
                cnt += 1
            else:
                current += i
            if cnt > m:
                res = False
                break
        return res
    
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0
        right = sum(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if self.smaller(nums, mid, m):
                right = mid
            else:
                left = mid
        if left == right:
            return left
        return left if self.smaller(nums, left, m) else right


# Solution 2: DP
# TLE
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         f = list()

#         sub = [0]
#         for i in nums:
#             sub.append(sub[-1] + i)

#         for i in range(n + 1):
#             f.append([float('inf')] * (m + 1))
#         f[0][0] = 0


#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 f[i][j] = min(max(f[k][j - 1], sub[i] - sub[k]) for k in range(i))

#         return f[n][m]

