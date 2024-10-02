import sys
from itertools import product
import copy


def getCCTVInfo(cctvMap):
    cctvInfo = []
    for r in range(rowSize):
        for c in range(colSize):
            if 0 < cctvMap[r][c] < 6:
                cctvInfo.append((cctvMap[r][c], r, c))
    return cctvInfo


def coverMapByCCTV(cctvMap, cctvInfo, direction):
    cctvType, r, c = cctvInfo
    dr, dc = direction
    if cctvType == 1:
        coverCCTVLine(cctvMap, r, c, dr, dc)
    elif cctvType == 2:
        coverCCTVLine(cctvMap, r, c, dr, dc)
        coverCCTVLine(cctvMap, r, c, -dr, -dc)
    elif cctvType == 3:
        coverCCTVLine(cctvMap, r, c, dr, dc)
        coverCCTVLine(cctvMap, r, c, -dc, dr)
    elif cctvType == 4:
        coverCCTVLine(cctvMap, r, c, dr, dc)
        coverCCTVLine(cctvMap, r, c, -dr, -dc)
        coverCCTVLine(cctvMap, r, c, dc, dr)
    elif cctvType == 5:
        coverCCTVLine(cctvMap, r, c, dr, dc)
        coverCCTVLine(cctvMap, r, c, -dr, -dc)
        coverCCTVLine(cctvMap, r, c, dc, dr)
        coverCCTVLine(cctvMap, r, c, -dc, -dr)


def coverCCTVLine(cctvMap, r, c, dr, dc):
    curR, curC = r, c
    while True:
        curR, curC = curR + dr, curC + dc
        if not (0 <= curR < rowSize and 0 <= curC < colSize) \
                or cctvMap[curR][curC] == 6:
            break
        if cctvMap[curR][curC] == 0:
            cctvMap[curR][curC] = 7


def findUncoveredArea(cctvMap):
    result = 0
    for r in cctvMap:
        result += r.count(0)
    return result


rowSize, colSize = map(int, sys.stdin.readline().split())
cctvMap = [list(map(int, sys.stdin.readline().split())) for i in range(rowSize)]

cctvInfoes = getCCTVInfo(cctvMap)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cases = product(directions, repeat=len(cctvInfoes))

result = 10000000

for case in cases:
    cur = result
    curCCTVMap = copy.deepcopy(cctvMap)
    for idx, direction in enumerate(case):
        coverMapByCCTV(curCCTVMap, cctvInfoes[idx], direction)
    result = min(result, findUncoveredArea(curCCTVMap))

print(result)