import sys
from collections import deque

def findMessNum(row, col, icebergs):
    messNum = 0
    visited = [[False for i in range(col)] for j in range(row)]

    for r in range(row):
        for c in range(col):
            if icebergs[r][c] > 0 and visited[r][c] == False:
                messNum += 1
                visited = bfs(row, col, (r, c), icebergs, visited)

    return messNum

def bfs(row, col, location, icebergs, visited):
    queue = deque()
    queue.append(location)
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and icebergs[nr][nc] > 0 and visited[nr][nc] == False:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return visited


def calculateMelting(row, col, icebergs):
    meltedList = []
    for r in range(row):
        for c in range(col):
            if icebergs[r][c] > 0:
                meltNum = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and icebergs[nr][nc] == 0:
                        meltNum += 1
                meltedList.append((r, c, meltNum))

    return meltedList


def melting(icebergs, meltedList):
    for r, c, meltNum in meltedList:
        icebergs[r][c] = max(icebergs[r][c] - meltNum, 0)

    return icebergs

def solution(row, col, icebergs):
    time = 0

    while True:
        messNum = findMessNum(row, col, icebergs)
        if messNum>= 2:
            return time
        elif messNum == 0:
            return 0

        meltedList = calculateMelting(row, col, icebergs)
        icebergs = melting(icebergs, meltedList)
        time += 1

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

row, col = map(int, sys.stdin.readline().split())
icebergs = [list(map(int, sys.stdin.readline().split())) for i in range(row)]

result = solution(row, col, icebergs)
print(result)
