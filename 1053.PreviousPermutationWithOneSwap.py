class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        stack = [n - 1]
        for i in range(n - 1, -1, -1):
            if A[i] <= A[stack[-1]]:
                stack.append(i)
                continue
            j = None
            while stack and A[i] > A[stack[-1]]:
                if j and A[j] == A[stack[-1]]:
                    break
                j = stack.pop()
            A[i], A[j] = A[j], A[i]
            return A
        return A

