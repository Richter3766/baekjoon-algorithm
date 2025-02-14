import sys
from collections import deque

def solution(maze_map):
    queue = deque()
    queue.append((0, 0))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row_size and 0 <= nc < col_size and maze_map[nr][nc] == 1:
                maze_map[nr][nc] += maze_map[r][c]
                queue.append((nr, nc))

    return maze_map[-1][-1]

row_size, col_size = map(int, sys.stdin.readline().split())
maze_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(row_size)]

result = solution(maze_map)

print(result)