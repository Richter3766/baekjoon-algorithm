import sys

def solution(numOfVertexes, infoOfEdges):
    weights = buildGraphAndWeights(numOfVertexes, infoOfEdges)

    minCost = findShortestPath(numOfVertexes, weights)

    return findCycle(numOfVertexes, minCost)

def buildGraphAndWeights(numOfVertexes, infoOfEdges):
    weights = [[float('inf') for i in range(numOfVertexes)] for i in range(numOfVertexes)]
    for start, end, weight in infoOfEdges:
        weights[start -1][end - 1] = min(weights[start -1][end - 1], weight)

    return weights


def findShortestPath(numOfVertexes, weights):
    for k in range(numOfVertexes):
        for r in range(numOfVertexes):
            for c in range(numOfVertexes):
                if weights[r][k] != float('inf') and weights[k][c] != float('inf'):
                    weights[r][c] = min(weights[r][c], weights[r][k] + weights[k][c])

    return weights


def findCycle(numOfVertexes, minCost):
    minCycleCost = float('inf')
    for i in range(numOfVertexes):
        if minCost[i][i] != float('inf'):
            minCycleCost = min(minCycleCost, minCost[i][i])

    if minCycleCost == float('inf'): return -1
    return minCycleCost

numOfVertexes, numOfEdges = map(int, sys.stdin.readline().split())
infoOfEdges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfEdges)]

result = solution(numOfVertexes, infoOfEdges)

print(result)