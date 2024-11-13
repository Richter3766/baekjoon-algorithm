import sys
import heapq

def initializeGraph(infoOfBuses):
    graph = [[] for i in range(numOfCities)]
    for s, e, w in infoOfBuses:
        graph[s - 1].append((w, e - 1))
    return graph


def findShortestPath(start, graph):
    costs = [float('inf')] * numOfCities
    costs[start] = 0
    queue = [(0, start)]

    while queue:
        cost, city = heapq.heappop(queue)
        if cost > costs[city]:
            continue

        for w, c in graph[city]:
            totalCost = cost + w
            if totalCost < costs[c]:
                costs[c] = totalCost
                heapq.heappush(queue, (totalCost, c))
    return costs


numOfCities = int(sys.stdin.readline())
numOfBuses = int(sys.stdin.readline())

infoOfBuses = [list(map(int, sys.stdin.readline().split())) for _ in range(numOfBuses)]
start, end = map(int, sys.stdin.readline().split())

graph = initializeGraph(infoOfBuses)
costs = findShortestPath(start - 1, graph)

print(costs[end - 1])