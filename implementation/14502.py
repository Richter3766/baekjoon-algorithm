import sys
from collections import deque
import copy
from itertools import combinations


def findEmptyAndVirusLocation():
    empty = []
    virus = []
    for r in range(rowSize):
        for c in range(colSize):
            if labMap[r][c] == 0:
                empty.append((r, c))
            elif labMap[r][c] == 2:
                virus.append((r, c))
    return empty, virus


def setCurLabMap(labMap, case):
    for r, c in case:
        labMap[r][c] = 1
    return labMap


def expandVirus(curLabMap):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for virus in virusLocation:
        queue = deque()
        queue.append(virus)
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rowSize and 0 <= nc < colSize and curLabMap[nr][nc] == 0:
                    curLabMap[nr][nc] = 2
                    queue.append((nr, nc))
    return curLabMap


def countZero(curLabMap):
    result = 0
    for row in curLabMap:
        result += row.count(0)
    return result


rowSize, colSize = map(int, sys.stdin.readline().split())
labMap = [list(map(int, sys.stdin.readline().split())) for i in range(rowSize)]

emptyLocation, virusLocation = findEmptyAndVirusLocation()
cases = combinations(emptyLocation, 3)

maxSafety = 0
for case in cases:
    curLabMap = setCurLabMap(copy.deepcopy(labMap), case)
    expandVirus(curLabMap)
    maxSafety = max(maxSafety, countZero(curLabMap))

print(maxSafety)