import sys
sys.setrecursionlimit(10 ** 6)

def dfs(row, col):
    if row == row_size - 1 and col == col_size - 1:
        return 1
    if dp_table[row][col] != -1:
        return dp_table[row][col]

    dp_table[row][col] = 0

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < row_size and 0 <= nc < col_size and road_map[nr][nc] < road_map[row][col]:
            dp_table[row][col] += dfs(nr, nc)

    return dp_table[row][col]

row_size, col_size = map(int, sys.stdin.readline().split())
road_map = [list(map(int, sys.stdin.readline().split())) for i in range(row_size)]

dp_table = [[-1] * col_size for _ in range(row_size)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = dfs(0, 0)

print(result)