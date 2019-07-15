class Solution:    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        
        def bfs(x, y):
            nonlocal board
            visit = [(x, y)]
            while visit:
                new = list()
                for cx, cy in visit:
                    board[cx][cy] = 'V'
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                            board[nx][ny] = 'V'
                            new.append((nx, ny))
                visit = new
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    bfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'V':
                    board[i][j] = 'O'
