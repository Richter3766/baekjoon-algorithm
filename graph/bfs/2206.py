import sys
from collections import deque


def bfs(row, col):
    queue = deque()
    queue.append((0, 0, 1, False))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[[False] * 2 for _ in range(col)] for _ in range(row)]
    visited[0][0][0] = True

    while queue:
        r, c, length, isBreak = queue.popleft()

        if r == row - 1 and c == col - 1:
            return length

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < row and 0 <= nc < col:
                if board[nr][nc] == 0 and not visited[nr][nc][isBreak]:
                    visited[nr][nc][isBreak] = True
                    queue.append((nr, nc, length + 1, isBreak))
                elif board[nr][nc] == 1 and not isBreak and not visited[nr][nc][1]:
                    visited[nr][nc][1] = True
                    queue.append((nr, nc, length + 1, True))

    return -1


row, col = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(row)]

minPath = bfs(row, col)

print(minPath)
