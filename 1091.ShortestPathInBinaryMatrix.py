class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        visit = [(0, 0)]
        visited = {(0, 0)}
        res = 1
        while visit:
            new = list()
            for x, y in visit:
                for dx, dy in [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        if (nx, ny) == (n - 1, n - 1):
                            return res + 1
                        new.append((nx, ny))
                        visited.add((nx, ny))
            visit = new
            res += 1

        return -1

