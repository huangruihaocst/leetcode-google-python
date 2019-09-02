from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(x):
            if x == 1:
                return False
            if x < 4:
                return True
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        cnt = 0
        for i in range(1, n + 1):
            if is_prime(i):
                cnt += 1
        print(cnt)
        return factorial(cnt) * factorial(n - cnt) % 1000000007
