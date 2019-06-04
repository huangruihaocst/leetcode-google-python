class Solution:
    def baseNeg2(self, N: int) -> str:
        neg = [2]
        for i in range(20):
            neg.append(neg[-1] << 2)
        for mask in neg:
            if mask & N:
                N += (mask << 1)
        return bin(N)[2:]

