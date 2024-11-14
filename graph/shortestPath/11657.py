import sys


def initializeGraph(edges):
    graph = [[] for i in range(numOfCities)]

    for start, end, weight in edges:
        graph[start - 1].append((weight, end - 1))

    return graph


def findShortestPath(graph):
    distances = [float('inf')] * numOfCities
    distances[0] = 0

    for _ in range(numOfCities - 1):
        for v in range(numOfCities):
            for weight, end in graph[v]:
                if distances[v] != float('inf') and distances[v] + weight < distances[end]:
                    distances[end] = distances[v] + weight

    for v in range(numOfCities):
        for weight, end in graph[v]:
            if distances[v] != float('inf') and distances[v] + weight < distances[end]:
                distances[end] = float('-inf')

    return distances


numOfCities, numOfEdges = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(numOfEdges)]

graph = initializeGraph(edges)

distances = findShortestPath(graph)

if float('-inf') in distances:
    print(-1)
else:
    for i in distances[1:]:
        if i != float('inf'): print(i)
        else: print(-1)
