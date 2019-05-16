# Union Search
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


# DFS
# class Solution:
#     def __init__(self):
#         self.graph = dict()

#     def add(self, v1, v2, val):
#         if v1 in self.graph:
#             self.graph[v1][v2] = val
#         else:
#             self.graph[v1] = {v2: val}

#     def query(self, v1, v2):
#         ans = None
#         current = 1
#         visited = {v1}

#         def visit(v):
#             nonlocal ans, current, visited
#             if v not in self.graph:
#                 return
#             if v == v2:
#                 ans = current
#                 return
#             for c in self.graph[v]:
#                 if c not in visited:
#                     visited.add(c)
#                     current *= self.graph[v][c]
#                     visit(c)
#                     visited.remove(c)
#                     current /= self.graph[v][c]

#         visit(v1)
#         return ans if ans is not None else -1

#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         n = len(equations)

#         # build graph
#         for i in range(n):
#             v1, v2 = equations[i]
#             val = values[i]
#             self.add(v1, v2, val)
#             self.add(v2, v1, 1 / val)

#         # query
#         res = list()
#         for v1, v2 in queries:
#             res.append(self.query(v1, v2))

#         return res
