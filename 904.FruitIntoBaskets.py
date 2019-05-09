class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        res = -1
        curr = 0
        prev, prev_cnt = None, 0
        prev2 = None
        for t in tree:
            if t == prev:
                curr += 1
                prev_cnt += 1
            elif t == prev2:
                prev2, prev = prev, prev2
                prev_cnt = 1
                curr += 1
            else:
                prev2, prev = prev, t
                curr = prev_cnt + 1
                prev_cnt = 1
            res = max(res, curr)
        return res
            
