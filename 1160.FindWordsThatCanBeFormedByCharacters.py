from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = Counter(chars)
        res = 0
        for w in words:
            word_counter = Counter(w)
            ok = True
            for c, v in word_counter.items():
                if c not in char_counter or v > char_counter[c]:
                    ok = False
                    break
            if ok:
                res += len(w)
        return res
