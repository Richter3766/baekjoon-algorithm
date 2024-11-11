import sys
import heapq

def initializeGraph(edges):
    graph = [[] for _ in range(numOfVertexes)]
    for s, e, w in edges:
        graph[s - 1].append((e - 1, w))
    return graph


def findShortestpath(start, graph):
    weights = [initial] * numOfVertexes
    weights[start - 1] = 0
    queue = [(0, start - 1)]

    while queue:
        w, s = heapq.heappop(queue)
        if w > weights[s]:
            continue

        for end, weight in graph[s]:
            distance = weight + w

            if distance < weights[end]:
                weights[end] = distance
                heapq.heappush(queue, (distance, end))

    return weights


numOfVertexes, numOfEdges = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
initial = float('inf')

edges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfEdges)]

graph = initializeGraph(edges)
weights = findShortestpath(start, graph)

for i in weights:
    if i == initial:
        print("INF")
    else:
        print(i)