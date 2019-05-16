class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        parent = dict()
        ans = dict()
        
        def find(x):
            nonlocal parent
            if parent[x] == x:
                return x
            else:
                root = find(parent[x])
                ans[x] *= ans[parent[x]]
                parent[x] = root
                return parent[x]
            
        def union(x, y, val):  # x / y = val
            parent.setdefault(x, x)
            ans.setdefault(x, 1)
            parent.setdefault(y, y)
            ans.setdefault(y, 1)
            x_root = find(x)
            y_root = find(y)
            if x_root != y_root:
                parent[x_root] = y_root
                ans[x_root] = ans[y] * val / ans[x]
        
        for i in range(n):
            v1, v2 = equations[i]
            val = values[i]
            union(v1, v2, val)
                    
        res = list()
        
        for v1, v2 in queries:
            if v1 not in parent or v2 not in parent:
                res.append(-1.0)
                continue
            if find(v1) != find(v2):
                res.append(-1.0)
                continue
            res.append(ans[v1] / ans[v2])
        
        return res

