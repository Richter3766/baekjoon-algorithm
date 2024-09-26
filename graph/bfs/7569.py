import sys
from collections import deque

def countUnripeAndRipeTomatoes():
    result = 0
    ripeTomatoes = []
    for h in range(height):
        for r in range(rowSize):
            for c in range(colSize):
                if tomatoes[h][r][c] == 0:
                    result += 1
                elif tomatoes[h][r][c] == 1:
                    ripeTomatoes.append((h, r, c, 0))

    return result, ripeTomatoes


def expandRipeTomatoes(ripeTomatoes):
    global numOfUnripeTomatoes
    queue = deque(ripeTomatoes)
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while queue:
        h, r, c, d = queue.popleft()
        for dh, dr, dc in directions:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 <= nh < height and \
                    0 <= nr < rowSize and \
                    0 <= nc < colSize and \
                    tomatoes[nh][nr][nc] == 0:
                tomatoes[nh][nr][nc] = d + 1
                queue.append((nh, nr, nc, d + 1))
                numOfUnripeTomatoes -= 1


def getTotalDays():
    days = 0
    for h in tomatoes:
        for r in h:
            days = max(days, max(r))
    return days


colSize, rowSize, height = map(int, sys.stdin.readline().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for i in range(rowSize)] for j in range(height)]

numOfUnripeTomatoes, ripeTomatoes = countUnripeAndRipeTomatoes()

if numOfUnripeTomatoes == 0:
    print(0)
else:
    expandRipeTomatoes(ripeTomatoes)
    if numOfUnripeTomatoes != 0:
        print(-1)
    else:
        print(getTotalDays())
