import sys
from collections import defaultdict, deque

numOfWorks = int(sys.stdin.readline())
infoOfWorks = [list(map(int, sys.stdin.readline().split())) for i in range(numOfWorks)]


def initializeGraph():
    completeTimes = [0] * (numOfWorks + 1)
    for i, work in enumerate(infoOfWorks):
        cost, numOfDependencies = work[0], work[1]
        completeTimes[i + 1] = cost

        for j in range(numOfDependencies):
            idx = j + 2
            indegrees[i + 1] += 1
            dependency[work[idx]].append(i + 1)
    return completeTimes

def findZeroIndegree():
    noDependency = deque()
    for i in range(1, numOfWorks + 1):
        if indegrees[i] == 0:
            noDependency.append(i)
    return noDependency


def calculateCost(noDependency, dependency, indegrees, completeTime):
    while noDependency:
        cur = noDependency.popleft()
        for i in dependency[cur]:
            indegrees[i] -= 1
            completeTime[i] = max(completeTime[i], completeTime[cur] + infoOfWorks[i - 1][0])

            if indegrees[i] == 0:
                noDependency.append(i)

    return max(completeTime)

dependency = defaultdict(list)
indegrees = [0 for i in range(numOfWorks + 1)]

completeTime = initializeGraph()
noDependency = findZeroIndegree()
result = calculateCost(noDependency, dependency, indegrees, completeTime)

print(result)