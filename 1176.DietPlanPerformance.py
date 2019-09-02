class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0
        days = 0
        n = len(calories)
        curr = 0
        for i in range(n):
            curr += calories[i]
            days += 1
            if days > k:
                curr -= calories[i - k]
                days -= 1
            if days == k:
                if curr < lower:
                    res -= 1
                elif curr > upper:
                    res += 1
        return res
