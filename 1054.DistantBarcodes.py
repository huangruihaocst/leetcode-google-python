from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        counter = Counter(barcodes)
        keys = counter.most_common()
        res = [None] * n
        pos = 0
        
        for k, v in keys:
            for i in range(v):
                if pos > n - 1:
                    pos = 1
                res[pos] = k
                pos += 2

        return res
        
