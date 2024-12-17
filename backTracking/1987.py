import sys


def backTracking(r, c, visited):
    maxDepth = len(visited)

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < row and 0 <= nc < col and board[nr][nc] not in visited:
            visited.add(board[nr][nc])
            maxDepth = max(maxDepth, backTracking(nr, nc, visited))
            visited.remove(board[nr][nc])

    return maxDepth


def solution(row, col, board):
    visited = set()
    visited.add(board[0][0])
    return backTracking(0, 0, visited)


row, col = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(row)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = solution(row, col, board)
print(result)
