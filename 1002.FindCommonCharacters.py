from collections import defaultdict
import string

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ds = list()
        for s in A:
            dd = defaultdict(lambda: 0)
            for c in s:
                dd[c] += 1
            ds.append(dd)
        res = list()
        for c in string.ascii_lowercase:
            times = min(dd[c] for dd in ds)
            res += [c] * times
        return res

