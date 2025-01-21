import sys
import heapq

def solution(numOfVertexes, numOfEdges, infoOfEdges):
    graph = build_graph(infoOfEdges, numOfVertexes)

    min_heap = [(0, 0)]
    visited = [False] * numOfVertexes

    weigths = 0
    while min_heap:
        current_weight, current_vertex = heapq.heappop(min_heap)
        if not visited[current_vertex]:
            weigths += current_weight
            visited[current_vertex] = True
            for adjusted_weight, adjusted_vertex in graph[current_vertex]:
                    heapq.heappush(min_heap, (adjusted_weight, adjusted_vertex))

    return weigths


def build_graph(infoOfEdges, numOfVertexes):
    graph = [[] for i in range(numOfVertexes)]

    for start, end, weight in infoOfEdges:
        graph[start - 1].append((weight, end - 1))
        graph[end - 1].append((weight, start - 1))

    return graph


numOfVertexes, numOfEdges = map(int, sys.stdin.readline().split())
infoOfEdges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfEdges)]

result = solution(numOfVertexes, numOfEdges, infoOfEdges)
print(result)