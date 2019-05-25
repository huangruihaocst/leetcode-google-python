class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        digits = list(map(str, range(k)))
        start = digits[0] * n
        visited = {start}
        current = list(start)
        target = k ** n
        
        def dfs(v):
            nonlocal visited, current
            
            # important DFS trick here.
            # use return True to skip further search,
            # thus save time
            if len(visited) == target:
                return True
            
            for d in digits:
                new = v[1:] + d
                if new not in visited:
                    visited.add(new)
                    current.append(d)
                    # also here: if answer has already been found,
                    # no need for further search
                    if dfs(new):
                        return True
                    visited.remove(new)
                    current.pop()
        
        if dfs(start):
            return ''.join(current)
        return str()

