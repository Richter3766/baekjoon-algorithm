import sys
from collections import deque
def dfs(row, col):
    global count

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = deque()
    stack.append((row, col))
    while stack:
        row, col = stack.pop()
        visited[row][col] = 1
        count += 1
        for drow, dcol in directions:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == 0 and trashMap[nrow][ncol] == 1:
                stack.append((nrow, ncol))
                visited[nrow][ncol] = 1


N, M, K = map(int, sys.stdin.readline().split())
trashes = [list(map(int, sys.stdin.readline().split())) for i in range(K)]

trashMap = [[0 for i in range(M)] for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]

for row, col in trashes:
    trashMap[row - 1][col - 1] = 1

result = []
count = 0
for row in range(N):
    for col in range(M):
        count = 0
        if visited[row][col] == 0 and trashMap[row][col] == 1:
            dfs(row, col)
            result.append(count)

print(max(result))