class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        start = sum(customers[i] * (1 - grumpy[i]) for i in range(n))
        
        loss = [customers[i] if grumpy[i] == 1 else 0 for i in range(n)]
        current = sum(loss[:X])
        _max = current
        i = 0
        while i < n - X:
            current = current - loss[i] + loss[i + X]
            _max = max(_max, current)
            i += 1
        
        return start + _max

