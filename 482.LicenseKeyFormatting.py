class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        joint = ''.join(S.split('-')).upper()
        remainder = len(joint) % K
        parts = list()
        if remainder > 0:
            parts.append(joint[:remainder])
        for i in range(len(joint) // K):
            parts.append(joint[remainder + i * K: remainder + (i + 1) * K])
        return '-'.join(parts)

