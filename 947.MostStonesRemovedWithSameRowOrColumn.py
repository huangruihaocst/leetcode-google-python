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

