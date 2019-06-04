class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = list()
        curr = 0
        for i in A:
            curr = (curr << 1) + i
            res.append(curr % 5 == 0)
        return res

