from collections import Counter
from itertools import combinations


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = Counter(frozenset(w) for w in words)
        res = list()
        for p in puzzles:
            curr = 0
            for k in range(len(p)):
                for c in combinations(p[1:], k):
                    curr += counter[frozenset(tuple(p[0]) + c)]
            res.append(curr)
        return res
