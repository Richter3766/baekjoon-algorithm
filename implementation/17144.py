import sys

def findCleanerLocation():
    for i in range(row):
        if dustMap[i][0] == -1:
           return i, i + 1


def calculatingExpandingDust():
    tempMap = [[0] * col for i in range(row)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(row):
        for c in range(col):
            if dustMap[r][c] > 0:
                expectedDustAmountExpanding = dustMap[r][c] // 5
                expandedNumber = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and dustMap[nr][nc] != -1:
                        expandedNumber += 1
                        tempMap[nr][nc] += expectedDustAmountExpanding
                dustMap[r][c] -= expectedDustAmountExpanding * expandedNumber
    return tempMap


def adjustExpandingDust(tempMap):
    for r in range(row):
        for c in range(col):
            dustMap[r][c] += tempMap[r][c]


def cleaningDustTop(cleanerTop):
    for i in range(cleanerTop - 1, 0, -1):
        dustMap[i][0] = dustMap[i - 1][0]
    for i in range(col - 1):
        dustMap[0][i] = dustMap[0][i + 1]
    for i in range(cleanerTop):
        dustMap[i][col - 1] = dustMap[i + 1][col - 1]
    for i in range(col - 1, 1, -1):
        dustMap[cleanerTop][i] = dustMap[cleanerTop][i - 1]
    dustMap[cleanerTop][1] = 0


def cleaningDustBottom(cleanerBottom):
    for i in range(cleanerBottom + 1, row - 1):
        dustMap[i][0] = dustMap[i + 1][0]
    for i in range(col - 1):
        dustMap[row - 1][i] = dustMap[row - 1][i + 1]
    for i in range(row - 1, cleanerBottom, -1):
        dustMap[i][col - 1] = dustMap[i - 1][col - 1]
    for i in range(col - 1, 1, -1):
        dustMap[cleanerBottom][i] = dustMap[cleanerBottom][i - 1]
    dustMap[cleanerBottom][1] = 0


def getTotalDust():
    result = 0
    for r in range(row):
        for c in range(col):
            if dustMap[r][c] != -1:
                result += dustMap[r][c]
    return result


row, col, timeRange = map(int, sys.stdin.readline().split())
dustMap = [list(map(int, sys.stdin.readline().split())) for i in range(row)]

cleanerTop, cleanerBottom = findCleanerLocation()

for t in range(timeRange):
    tempMap = calculatingExpandingDust()
    adjustExpandingDust(tempMap)
    cleaningDustTop(cleanerTop)
    cleaningDustBottom(cleanerBottom)

result = getTotalDust()
print(result)