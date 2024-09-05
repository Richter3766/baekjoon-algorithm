import sys
from collections import defaultdict, deque


def makeGraph():
    for buildingNumber in range(1, numOfBuildings + 1):
        buildingInfo = buildingInfos[buildingNumber - 1]

        buildingTimes[buildingNumber] = buildingInfo[0]
        for info in buildingInfo[1:]:
            if info == -1:
                break
            graph[info].append(buildingNumber)
            inDegree[buildingNumber] += 1


def findTotalBuildTime():
    queue = deque([node for node in range(1, numOfBuildings + 1) if inDegree[node] == 0])
    result = [0] * (numOfBuildings + 1)

    while queue:
        node = queue.popleft()
        result[node] += buildingTimes[node]

        for neighbor in graph[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.appendleft(neighbor)
            result[neighbor] = max(result[neighbor], result[node])

    return result


def printResult(result):
    for i in range(1, numOfBuildings + 1):
        print(result[i])


numOfBuildings = int(sys.stdin.readline())
buildingInfos = [list(map(int, sys.stdin.readline().split())) for i in range(numOfBuildings)]

graph = defaultdict(list)
inDegree = [0] * (numOfBuildings + 1)
buildingTimes = [0] * (numOfBuildings + 1)

makeGraph()
result = findTotalBuildTime()
printResult(result)