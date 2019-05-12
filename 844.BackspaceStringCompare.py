class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        back_s, back_t = 0, 0
        
        while i >= 0 or j >= 0:
            if i >= 0 and S[i] == '#':
                i -= 1
                back_s += 1
                continue
            if j >= 0 and T[j] == '#':
                j -= 1
                back_t += 1
                continue
            if back_s > 0:
                i -= 1
                back_s -= 1
                continue
            if back_t > 0:
                j -= 1
                back_t -= 1
                continue
            if back_s == 0 and back_t == 0:
                if S[i] != T[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
            
        return True

