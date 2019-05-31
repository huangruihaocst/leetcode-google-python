# Solution 1: straightforward
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s: str, t: str) -> bool:
            d = dict()
            for c1, c2 in zip(s, t):
                if c1 not in d:
                    d[c1] = c2
                else:
                    if d[c1] != c2:
                        return False
            return True
        return check(s, t) and check(t, s)


# Solution 2: 1-line
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))