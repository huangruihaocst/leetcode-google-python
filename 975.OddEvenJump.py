class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
        next_greater = [-1] * len(A)
        next_smaller = [-1] * len(A)
        
        stack = list()
        
        for v, i in sorted([v, i] for i, v in enumerate(A)):
            while stack and stack[-1] < i:
                next_greater[stack.pop()] = i
            stack.append(i)
            
        stack = list()
        
        for v, i in sorted([-v, i] for i, v in enumerate(A)):
            while stack and stack[-1] < i:
                next_smaller[stack.pop()] = i
            stack.append(i)
            
        odd = [0] * (len(A) - 1) + [1]
        even = [0] * (len(A) - 1) + [1]
        
        for i in range(len(A) - 2, -1, -1):
            odd[i] = even[next_greater[i]] if next_greater[i] != -1 else 0
            even[i] = odd[next_smaller[i]] if next_smaller[i] != -1 else 0
            
        return sum(odd)
        