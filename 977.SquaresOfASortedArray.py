class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1
        res = list()
        while right > left and A[left] <= 0 and A[right] >= 0:
            if A[right] > -A[left]:
                res.append(A[right] * A[right])
                right -= 1
            else:
                res.append(A[left] * A[left])
                left += 1

        if A[left] >= 0:
            while right >= left:
                res.append(A[right] * A[right])
                right -= 1
        elif A[right] <= 0:
            while right >= left:
                res.append(A[left] * A[left])
                left += 1

        return res[::-1]

