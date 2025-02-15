import sys

def solution(drawing_map):
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    num_drawing = 0
    largest_size = 0

    for r in range(row_size):
        for c in range(col_size):
            if drawing_map[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                num_drawing += 1
                drawing_size = dfs(drawing_map, visited, r, c)
                largest_size = max(largest_size, drawing_size)

    return num_drawing, largest_size


def dfs(drawing_map, visited, row, col):
    stack = [(row, col)]
    drawing_size = 1
    directinos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        r, c = stack.pop()

        for dr, dc in directinos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row_size and 0 <= nc < col_size and drawing_map[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
                drawing_size += 1

    return drawing_size


row_size, col_size = map(int, sys.stdin.readline().split())
drawing_map = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]

num_drawing, largest_size = solution(drawing_map)

print(num_drawing)
print(largest_size)