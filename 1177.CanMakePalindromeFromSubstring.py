class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0] * 26]
        for i in range(1, len(s) + 1):
            prefix.append(prefix[-1][:])
            prefix[i][ord(s[i - 1]) - ord('a')] += 1
        res = list()
        for left, right, k in queries:
            l, r = prefix[left], prefix[right + 1]
            diff = [r[i] - l[i] for i in range(26)]
            res.append(sum(1 for i in diff if i % 2 == 1) // 2 <= k)
        return res
