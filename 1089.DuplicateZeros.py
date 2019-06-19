# Solution 1: space O(1), time O(n).
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        j = n + arr.count(0)
        i = n - 1
        while i >= 0:
            j -= 1
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1


# Solution 2: space O(1), time O(n ^ 2).
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         i = 0
#         while i < len(arr) - 1:
#             if arr[i] == 0:
#                 for j in range(len(arr) - 1, i + 1, -1):
#                     arr[j] = arr[j - 1]
#                 arr[i + 1] = 0
#                 i += 2
#             else:
#                 i += 1
