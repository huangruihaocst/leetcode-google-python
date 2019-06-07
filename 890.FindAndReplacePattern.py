class Solution:
    def to_list(w: str) -> List[int]:
        i = 0
        d = dict()
        res = list()
        for c in w:
            if c not in d:
                d[c] = i
                i += 1
            res.append(d[c])
        return res      
    
    @staticmethod
    def check(w1: str, w2: str) -> bool:
        return Solution.to_list(w1) == Solution.to_list(w2)
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return list(filter(lambda w: Solution.check(w, pattern), words))

