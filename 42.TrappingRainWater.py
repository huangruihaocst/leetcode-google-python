class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left = [0]
        for i in range(1, n):
            left.append(max(height[i - 1], left[-1]))
        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])
        res = 0
        for i in range(n):
            tmp = min(left[i], right[i]) - height[i]
            if tmp > 0:
                res += tmp
        return res
