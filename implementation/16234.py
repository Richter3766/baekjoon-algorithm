import sys
from collections import deque

def checkPossibleMigration(countryMap):
    unionList = []
    unionPopulationList = []

    visited = [[0 for i in range(sizeN)] for i in range(sizeN)]

    unionIdx = 0
    for row in range(sizeN):
        for col in range(sizeN):
            if visited[row][col] == 0:
                unionList.append([(row, col)])
                visited, unionList, unionPopulaion = findUnion(countryMap, row, col, visited, unionList, unionIdx)
                unionPopulationList.append(unionPopulaion)
                unionIdx += 1

    return unionList, unionPopulationList


def findUnion(countryMap, row, col, visited, unionList, unionIdx):
    visited[row][col] = 1

    queue = deque()
    queue.append((row, col))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    unionPopulation = countryMap[row][col]
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < sizeN and 0 <= nx < sizeN and visited[ny][nx] == 0 \
                    and lowCap <= abs(countryMap[y][x] - countryMap[ny][nx]) <= highCap:
                visited[ny][nx] = 1
                unionList[unionIdx].append((ny, nx))
                queue.append((ny, nx))
                unionPopulation += countryMap[ny][nx]
    return visited, unionList, unionPopulation

def changePopulationOfCountry(countryMap, unionList, unionPopulationList):
    for idx, union in enumerate(unionList):
        if len(union) > 1:
            curPopulation = unionPopulationList[idx] // len(union)
            for y, x in union:
                countryMap[y][x] = curPopulation

    return countryMap


sizeN, lowCap, highCap = map(int, sys.stdin.readline().split())
countryMap = [list(map(int, sys.stdin.readline().split())) for i in range(sizeN)]

migrationDay = 0
while True:
    unionList, unionPopulationList = checkPossibleMigration(countryMap)

    if all(len(i) == 1 for i in unionList ):
        break

    countryMap = changePopulationOfCountry(countryMap, unionList, unionPopulationList)
    migrationDay += 1

print(migrationDay)