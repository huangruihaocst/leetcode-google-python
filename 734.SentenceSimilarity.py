class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        d = dict()
        for w1, w2 in pairs:
            if w1 in d:
                d[w1].add(w2)
            else:
                d[w1] = {w2}
            if w2 in d:
                d[w2].add(w1)
            else:
                d[w2] = {w1}
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or (w1 in d and w2 in d[w1]) or (w2 in d and w1 in d[w2]):
                continue
            else:
                return False
        return True

