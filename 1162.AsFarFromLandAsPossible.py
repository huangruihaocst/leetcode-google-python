# Solution 1: AC.
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visit = list()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    visit.append((i, j))
        if len(visit) == 0 or len(visit) == row * col:
            return -1
        layer = 0
        while visit:
            new = list()
            for x, y in visit:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        new.append((nx, ny))
                        grid[nx][ny] = 1
            layer += 1
            visit = new
        return layer - 1

# Solution 2: TLE.
# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         row, col = len(grid), len(grid[0])
#         s = sum(grid[i][j] for i in range(row) for j in range(col))
#         if s == 0 or s == row * col:
#             return -1
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == 1:
#                     grid[i][j] = None
#                 else:
#                     grid[i][j] = list()
                    
#         def cal(x, y, cnt):
#             visit = {(x, y)}
#             level = 1
#             while visit:
#                 new = set()
#                 for vx, vy in visit:
#                     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                         nx, ny = vx + dx, vy + dy
#                         if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] is not None and len(grid[nx][ny]) < cnt:
#                             grid[nx][ny].append(level)
#                             new.add((nx, ny))
#                 level += 1
#                 visit = new
                    
#         cnt = 1
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] is None:
#                     cal(i, j, cnt)
#                     cnt += 1
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] is not None:
#                     grid[i][j] = min(grid[i][j])
#                 else:
#                     grid[i][j] = -1
#         return max(grid[i][j] for i in range(row) for j in range(col))
