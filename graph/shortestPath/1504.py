import sys
import heapq


def solution(numOfVertexes, numOfEdges, infoOfEdges, must1, must2):
    graph = buildGraph(numOfVertexes, infoOfEdges)

    startPath = findShortestPath(numOfVertexes, 0, graph)
    must1Path = findShortestPath(numOfVertexes, must1, graph)
    must2Path = findShortestPath(numOfVertexes, must2, graph)

    limit = float('inf')
    if any(limit in path for path in [startPath, must1Path, must2Path]):
        return -1

    return min(startPath[must1] + must1Path[must2] + must2Path[-1],
               startPath[must2] + must2Path[must1] + must1Path[-1])


def buildGraph(numOfVertexes, infoOfEdges):
    graph = [[] for i in range(numOfVertexes)]

    for start, end, cost in infoOfEdges:
        graph[start - 1].append((cost, end - 1))
        graph[end - 1].append((cost, start - 1))

    return graph


def findShortestPath(numOfVertexes, start, graph):
    weights = [float('inf')] * numOfVertexes
    weights[start] = 0

    queue = []
    queue.append((0, start))

    while queue:
        cost, cur = heapq.heappop(queue)

        if cost > weights[cur]:
            continue

        for weight, end in graph[cur]:
            if weight + cost < weights[end]:
                weights[end] = weight + cost
                heapq.heappush(queue, (weight + cost, end))

    return weights


numOfVertexes, numOfEdges = map(int, sys.stdin.readline().split())
infoOfEdges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfEdges)]
must1, must2 = map(int, sys.stdin.readline().split())

result = solution(numOfVertexes, numOfEdges, infoOfEdges, must1 - 1, must2 - 1)
print(result)