from collections import defaultdict
from copy import deepcopy

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        row, col = len(board), len(board[0])
        
        def crash(board: List[List[int]]) -> bool:
            s = set()

            def check(x: int, y: int):
                nonlocal s
                if x < row - 2 and board[x][y] == board[x + 1][y] == board[x + 2][y]:
                    s.add((x, y))
                    s.add((x + 1, y))
                    s.add((x + 2, y))
                    t = x + 3
                    while t < row and board[t][y] == board[x][y]:
                        s.add((t, y))
                        t += 1
                if y < col - 2 and board[x][y] == board[x][y + 1] == board[x][y + 2]:
                    s.add((x, y))
                    s.add((x, y + 1))
                    s.add((x, y + 2))
                    t = y + 3
                    while t < col and board[x][t] == board[x][y]:
                        s.add((x, t))
                        t += 1

            crashed = defaultdict(set)
            for i in range(row):
                for j in range(col):
                    if board[i][j] != 0:
                        check(i, j)
            for x, y in s:
                crashed[y].add(x)
            
            if len(crashed) == 0:
                return False
            for y in crashed:
                i, j = row - 1, row - 1
                while j < row:
                    while j >= 0 and j in crashed[y]:
                        j -= 1
                    if j < 0:
                        break
                    board[i][y] = board[j][y]
                    i -= 1
                    j -= 1
                while i >= 0:
                    board[i][y] = 0
                    i -= 1
            return True

        found = True
        while found:
            found = crash(board)
        return board
        
        
