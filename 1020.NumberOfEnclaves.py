# Solution 1: BFS
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])

        def bfs(x, y):
            A[x][y] = 0
            visit = [(x, y)]
            while visit:
                new = list()
                for _x, _y in visit:
                    for dx, dy in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                        nx, ny = _x + dx, _y + dy
                        if 0 <= nx < r and 0 <= ny < c and A[nx][ny] == 1:
                            A[nx][ny] = 0
                            new.append((nx, ny))
                visit = new

        for row in range(r):
            for col in range(c):
                if (row == 0 or row == r - 1 or col == 0 or col == c - 1) and A[row][col] == 1:
                    bfs(row, col)

        return sum(sum(row) for row in A)


# Solution 2: DFS
# class Solution:
#     def numEnclaves(self, A: List[List[int]]) -> int:
#         r, c = len(A), len(A[0])

#         def dfs(x, y):
#             A[x][y] = 0
#             for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < r and 0 <= ny < c and A[nx][ny] == 1:
#                     dfs(nx, ny)

#         for row in range(r):
#             for col in range(c):
#                 if A[row][col] == 1 and (row == 0 or row == r - 1 or col == 0 or col == c - 1):
#                     dfs(row, col)

#         return sum(sum(row) for row in A)
