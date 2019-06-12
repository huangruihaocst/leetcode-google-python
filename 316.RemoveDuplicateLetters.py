# Solution 1: Greedy. Beat 13%.
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
            return str()
        counter = Counter(s)
        pos = 0
        for i, c in enumerate(s):
            if s[pos] > c:
                pos = i
            counter[c] -= 1
            if counter[c] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ''))


# Solution 2: See Problem #1081.