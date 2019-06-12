class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = dict()
        for i, c in enumerate(text):
            last[c] = i
        stack = list()
        has = set()
        for i, c in enumerate(text):
            if c in has:
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                has.remove(stack[-1])
                stack.pop()
            stack.append(c)
            has.add(c)
        return ''.join(stack)

