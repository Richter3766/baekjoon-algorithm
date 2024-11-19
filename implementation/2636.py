import sys
from collections import deque


def bfs(cheeseMap):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    deleted = []
    queue = deque()
    queue.append((0, 0))
    visited = [[0 for i in range(colSize)] for i in range(rowSize)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rowSize and 0 <= nc < colSize and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if cheeseMap[nr][nc] == 1:
                    deleted.append((nr, nc))
                elif cheeseMap[nr][nc] == 0:
                    queue.append((nr, nc))
    return deleted


def deleteCheese(cheeseMap, cheeseWillDelete):
    for r, c in cheeseWillDelete:
        cheeseMap[r][c] = 0

rowSize, colSize = map(int, sys.stdin.readline().split())
cheeseMap = [list(map(int, sys.stdin.readline().split())) for _ in range(rowSize)]

days = 0
lastCheese = 0
while True:
    cheeseWillDelete = bfs(cheeseMap)

    if len(cheeseWillDelete) == 0:
        break
    deleteCheese(cheeseMap, cheeseWillDelete)

    lastCheese = len(cheeseWillDelete)
    days += 1

print(days)
print(lastCheese)