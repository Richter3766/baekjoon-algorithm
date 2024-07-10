import sys

sys.setrecursionlimit(10000)

rowSize, colSize = map(int, sys.stdin.readline().split())
pointBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(rowSize)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(row, col, depth, total):
    global result
    if depth == 4:
        result = max(result, total)
        return
    for drow, dcol in directions:
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < rowSize and 0 <= ncol < colSize and not visited[nrow][ncol]:
            visited[nrow][ncol] = True
            dfs(nrow, ncol, depth + 1, total + pointBoard[nrow][ncol])
            visited[nrow][ncol] = False

def check_special_shape(row, col):
    global result
    for shape in special_shapes:
        try:
            total = pointBoard[row][col] + pointBoard[row + shape[0][0]][col + shape[0][1]] + pointBoard[row + shape[1][0]][col + shape[1][1]] + pointBoard[row + shape[2][0]][col + shape[2][1]]
            result = max(result, total)
        except IndexError:
            continue

result = 0
visited = [[False] * colSize for _ in range(rowSize)]

special_shapes = [
    [(0, 1), (0, 2), (-1, 1)],  # ㅗ
    [(0, 1), (0, 2), (1, 1)],   # ㅜ
    [(1, 0), (2, 0), (1, -1)],  # ㅓ
    [(1, 0), (2, 0), (1, 1)]    # ㅏ
]

for row in range(rowSize):
    for col in range(colSize):
        visited[row][col] = True
        dfs(row, col, 1, pointBoard[row][col])
        visited[row][col] = False
        check_special_shape(row, col)

print(result)
