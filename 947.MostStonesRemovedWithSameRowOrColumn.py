# Solution 1: build graph from dictionary. Then DFS.
# Time: O(n).
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = dict()
        x_coordinates = dict()
        y_coordinates = dict()
        
        for i, coordinate in enumerate(stones):
            x, y = coordinate
            if x not in x_coordinates:
                x_coordinates[x] = {i}
            else:
                x_coordinates[x].add(i)
            if y not in y_coordinates:
                y_coordinates[y] = {i}
            else:
                y_coordinates[y].add(i)
        
        for i in range(len(stones)):
            graph[i] = x_coordinates[stones[i][0]].union(y_coordinates[stones[i][1]])
            graph[i].remove(i)
            
        visited = set()    
        def dfs(stone):
            nonlocal visited
            visited.add(stone)
            children = graph[stone]
            for c in children:
                if c not in visited:
                    dfs(c)
            
        islands = 0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                islands += 1
        return len(stones) - islands


# Solution 2: build graph from dictionary. Then union search.
# Time: O(n).
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         graph = dict()
#         x_coordinates = dict()
#         y_coordinates = dict()
        
#         for i, coordinate in enumerate(stones):
#             x, y = coordinate
#             if x not in x_coordinates:
#                 x_coordinates[x] = {i}
#             else:
#                 x_coordinates[x].add(i)
#             if y not in y_coordinates:
#                 y_coordinates[y] = {i}
#             else:
#                 y_coordinates[y].add(i)
        
#         for i in range(len(stones)):
#             graph[i] = x_coordinates[stones[i][0]].union(y_coordinates[stones[i][1]])
#             graph[i].remove(i)
            
#         parent = list(range(len(stones)))
#         rank = [0] * len(stones)
#         count = len(stones)
        
#         def find(i):
#             nonlocal parent
#             if i == parent[i]:
#                 return i
#             else:
#                 parent[i] = find(parent[i])
#                 return parent[i]
        
#         def union(i, j):
#             nonlocal count
#             i = find(i)
#             j = find(j)
#             if i != j:
#                 if rank[i] > rank[j]:
#                     parent[j] = i
#                 else:
#                     if rank[i] == rank[j]:
#                         rank[i] += 1
#                     parent[i] = j
#                 count -= 1
        
#         for node, children in graph.items():
#             for c in children:
#                 union(node, c)
        
#         return len(stones) - count


# Solution 3: union search. Treat row and column index as the same kind of index.
# row -> row, column -> ~column.
# Time: O(n).
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         parent = dict()
        
#         def find(i):
#             nonlocal parent
#             if i == parent[i]:
#                 return i
#             else:
#                 parent[i] = find(parent[i])
#                 return parent[i]
        
#         def union(i, j):
#             nonlocal parent
#             parent.setdefault(i, i)
#             parent.setdefault(j, j)
#             parent[find(i)] = find(j)
        
#         for i, j in stones:
#             union(i, ~j)
        
#         return len(stones) - len({find(i) for i, j in stones})


