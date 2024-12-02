import sys
from collections import defaultdict, deque
import copy

def buildInfoOfTC(numOfTC):
    infoOfTC = [[] for i in range(numOfTC)]

    for i in range(numOfTC):
        numOfBuildings, numOfRules = map(int, sys.stdin.readline().split())
        costOfBuildings = list(map(int, sys.stdin.readline().split()))
        dependency = [list(map(int, sys.stdin.readline().split())) for i in range(numOfRules)]
        target = int(sys.stdin.readline())
        infoOfTC[i].append((numOfBuildings, numOfRules))
        infoOfTC[i].append(costOfBuildings)
        infoOfTC[i].append(dependency)
        infoOfTC[i].append(target)

    return infoOfTC


def topologicalSort(numOfBuildings, dependency):
    indegree = [0] * numOfBuildings
    indegreeGraph = defaultdict(list)
    outDegree = defaultdict(list)
    result = []

    for start, end in dependency:
        indegree[end - 1] += 1
        outDegree[start - 1].append(end - 1)
        indegreeGraph[end - 1].append(start - 1)

    queue = deque()
    for i in range(numOfBuildings):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        result.append(cur)
        for end in outDegree[cur]:
            indegree[end] -= 1
            if indegree[end] == 0:
                queue.append(end)

    return result, indegreeGraph


def solution(numOfTC, infoOfTC):
    numOfBuildings, numOfRules = infoOfTC[0]
    costOfBuildings, dependency, target = infoOfTC[1], infoOfTC[2], infoOfTC[3]

    buildOrder, indegree = topologicalSort(numOfBuildings, dependency)
    dp = copy.deepcopy(costOfBuildings)

    for i in buildOrder:
        maxCost = 0
        for j in indegree[i]:
            maxCost = max(maxCost, dp[j])
        dp[i] += maxCost

    return dp[target - 1]


numOfTC = int(sys.stdin.readline())
infoOfTC = buildInfoOfTC(numOfTC)


for i in range(numOfTC):
    result = solution(numOfTC, infoOfTC[i])
    print(result)