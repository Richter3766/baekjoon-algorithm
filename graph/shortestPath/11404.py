import sys

numOfCities = int(sys.stdin.readline())
numOfBuses = int(sys.stdin.readline())
infoOfBuses = [list(map(int, sys.stdin.readline().split())) for _ in range(numOfBuses)]

INF = float('inf')
costList = [[INF for i in range(numOfCities)] for _ in range(numOfCities)]

for start, end, cost in infoOfBuses:
    start -= 1
    end -= 1
    costList[start][end] = min(costList[start][end], cost)

for k in range(numOfCities):
    for r in range(numOfCities):
        for c in range(numOfCities):
            if costList[r][k] < INF and costList[k][c] < INF:
                costList[r][c] = min(costList[r][c], costList[r][k] + costList[k][c])

for r in range(numOfCities):
    for c in range(numOfCities):
        if r == c or costList[r][c] == INF:
            print(0, end=" ")
        else:
            print(costList[r][c], end=" ")
    print()