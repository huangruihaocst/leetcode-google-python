class Solution:
    def lastSubstring(self, s: str) -> str:
        last = s[0]
        candidate = str()
        j = 0
        for i in range(1, len(s)):
            if s[i] > last:
                last = s[i]
                candidate = str()
                j = 0
            else:
                if s[i] == last[j]:
                    candidate += s[i]
                    last += s[i]
                    j += 1
                else:
                    if candidate:
                        if candidate + s[i] > last:
                            last = candidate + s[i]
                        else:
                            last += s[i]
                        candidate = str()
                        j = 0
                    else:
                        last += s[i]
        return last
