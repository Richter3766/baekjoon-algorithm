import sys
from collections import deque

def countCheese():
    cnt = 0
    for r in range(rowSize):
        for c in range(colSize):
            if cheeseMap[r][c] == 1:
                cnt += 1
    return cnt


def findMeltingCheese():
    cntCheeseMeetAir = [[0] * colSize for i in range(rowSize)]
    visited = [[0] * colSize for i in range(rowSize)]
    queue = deque()
    queue.append((0, 0))
    meltingCheese = set()

    while queue:
        r, c = queue.popleft()
        if visited[r][c] == 1:
            continue

        visited[r][c] = 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rowSize and 0 <= nc < colSize and visited[nr][nc] == 0:
                if  cheeseMap[nr][nc] == 0:
                    queue.append((nr, nc))
                elif cheeseMap[nr][nc] == 1:
                    cntCheeseMeetAir[nr][nc] += 1
                    if cntCheeseMeetAir[nr][nc] >= 2:
                        meltingCheese.add((nr, nc))


    return meltingCheese


def deleteMeltingCheese(meltingCheese):
    for r, c in meltingCheese:
        cheeseMap[r][c] = 0


rowSize, colSize = map(int, sys.stdin.readline().split())
cheeseMap = [list(map(int, sys.stdin.readline().split())) for i in range(rowSize)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0
cheeseCount = countCheese()
while cheeseCount > 0:
    meltingCheese = findMeltingCheese()
    deleteMeltingCheese(meltingCheese)
    cheeseCount -= len(meltingCheese)
    result += 1

print(result)