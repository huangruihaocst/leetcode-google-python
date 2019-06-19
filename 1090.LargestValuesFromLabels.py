from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        combined = sorted(zip(values, labels), reverse=True)
        counter = defaultdict(lambda: 0)
        res, cnt = 0, 0
        for v, l in combined:
            if cnt < num_wanted and counter[l] < use_limit:
                res += v
                counter[l] += 1
                cnt += 1
        return res

