import sys
import copy
import heapq

def initializeGraph(edges):
    graph = [[] for i in range(numOfMen)]
    for start, end, distance in edges:
        graph[start - 1].append((distance, end - 1))
    return graph


def findShortestPath(start, graph):
    INF = float('inf')
    distances = [INF] * numOfMen
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, node = heapq.heappop(queue)
        if distance > distances[node]:
            continue

        for dist, end in graph[node]:
            distanceSum = distance + dist
            if distanceSum < distances[end]:
                distances[end] = distanceSum
                heapq.heappush(queue, (distanceSum, end))

    return distances

numOfMen, numOfEdges, destination = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfEdges)]

graph = initializeGraph(edges)
returnRoutes = findShortestPath(destination - 1, graph)

maxTime = 0
for i in range(numOfMen):
    routes = findShortestPath(i, graph)
    totalTime = routes[destination - 1] + returnRoutes[i]
    maxTime = max(maxTime, totalTime)

print(maxTime)