# Solution 1: not using cache (cache S's splitting result)
class Solution:
    @staticmethod
    def next_counter(s: str, start: int) -> (str, int):
        cnt = 1
        while start + cnt < len(s) and s[start + cnt] == s[start]:
            cnt += 1
        return s[start], cnt
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i, j = 0, 0
            while i < len(word) and j < len(S):
                c0, cnt0 = Solution.next_counter(word, i)
                c1, cnt1 = Solution.next_counter(S, j)
                if c0 == c1 and ((cnt0 < cnt1 and cnt1 >= 3) or cnt0 == cnt1):
                    i += cnt0
                    j += cnt1
                else:
                    break
            if i == len(word) and j == len(S):
                res += 1
        return res


# Solution 2: using cache
# class Solution:
#     @staticmethod
#     def to_counter(s: str) -> List[tuple]:
#         counter = list()
#         i = 0
#         while i < len(s):
#             cnt = 1
#             while i + cnt < len(s) and s[i + cnt] == s[i]:
#                 cnt += 1
#             counter.append((s[i], cnt))
#             i += cnt
#         return counter
    
#     def expressiveWords(self, S: str, words: List[str]) -> int:
#         res = 0
#         counter_s = Solution.to_counter(S)
#         for word in words:
#             counter_word = Solution.to_counter(word)
#             if len(counter_s) != len(counter_word):
#                 continue
#             expressive = True
#             for (c0, cnt0), (c1, cnt1) in zip(counter_word, counter_s):
#                 if c0 != c1 or ((cnt0 >= cnt1 or cnt1 < 3) and cnt0 != cnt1):
#                     expressive = False
#                     break
#             if expressive:
#                 res += 1
#         return res
