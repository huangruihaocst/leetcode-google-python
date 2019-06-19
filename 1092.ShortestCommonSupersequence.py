# Solution 1: Longest common sub-sequence. DP.
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def LCS(str1: str, str2: str) -> str:
            dp = [[None for i in range(len(str2))] for j in range(len(str1))]
            for i in range(len(str1)):
                for j in range(len(str2)):
                    if i == 0:
                        dp[i][j] = str1[0] if str1[0] in str2[:j + 1] else str()
                        continue
                    if j == 0:
                        dp[i][j] = str2[0] if str2[0] in str1[:i + 1] else str()
                        continue
                    if str1[i] == str2[j]:
                        dp[i][j] = dp[i - 1][j - 1] + str1[i]
                    else:
                        if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                            dp[i][j] = dp[i - 1][j]
                        else:
                            dp[i][j] = dp[i][j - 1]
            return dp[-1][-1]
        
        i, j = 0, 0
        res = str()
        for c in LCS(str1, str2):
            while i < len(str1) and str1[i] != c:
                res += str1[i]
                i += 1
            while j < len(str2) and str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        res += str1[i:] + str2[j:]
        return res


# Solution 2: Shortest common super string. DP.
# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         l1, l2 = len(str1), len(str2)
#         dp = [[None for i in range(l2 + 1)] for j in range(l1 + 1)]
#         dp[-1][-1] = str()
#         dp[-1][-2] = str2[-1]
#         dp[-2][-1] = str1[-1]
        
#         for i in range(l1, -1, -1):
#             for j in range(l2, -1, -1):
#                 if i == l1 and j == l2:
#                     continue
#                 if i == l1:
#                     dp[i][j] = str2[j] + dp[i][j + 1]
#                 elif j == l2:
#                     dp[i][j] = str1[i] + dp[i + 1][j]
#                 else:
#                     if str1[i] == str2[j]:
#                         dp[i][j] = str1[i] + dp[i + 1][j + 1]
#                     else:
#                         dp[i][j] = str2[j] + dp[i][j + 1] if len(dp[i + 1][j]) > len(dp[i][j + 1]) else str1[i] + dp[i + 1][j]
#                     if i + 2 <= l1:
#                         dp[i + 2] = None
        
#         return dp[0][0]

