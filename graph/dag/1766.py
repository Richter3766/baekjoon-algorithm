import sys
from collections import defaultdict
import heapq


def makeGraph():
    for start, end in preProblems:
        graph[start].append(end)
        inDegree[end] += 1


def solveProblem():
    queue = [node for node in range(1, numOfProblem + 1) if inDegree[node] == 0]
    heapq.heapify(queue)

    result = []
    while queue:
        node = heapq.heappop(queue)
        result.append(node)

        for neighbor in graph[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                heapq.heappush(queue, neighbor)

    return result


numOfProblem, numOfPreProblem = map(int, sys.stdin.readline().split())
preProblems = [list(map(int, sys.stdin.readline().split())) for i in range(numOfPreProblem)]

graph = defaultdict(list)
inDegree = [0] * (numOfProblem + 1)

makeGraph()
result = solveProblem()

print(' '.join(map(str, result)))