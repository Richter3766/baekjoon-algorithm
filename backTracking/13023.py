import sys
from collections import defaultdict
from random import vonmisesvariate

sys.setrecursionlimit(10**4)

def buildGraph(numOfPeople, infoOfEdges):
    graph = defaultdict(list)
    for start, end in infoOfEdges:
        graph[start].append(end)
        graph[end].append(start)
    return graph

def dfs(graph, current, depth, visited):
    if depth == 5:
        return True

    visited[current] = True
    for friend in graph[current]:
        if not visited[friend]:
            if dfs(graph, friend, depth + 1, visited):
                return True
    visited[current] = False
    return False


def solution(numOfPeople, infoOfEdges):
    graph = buildGraph(numOfPeople, infoOfEdges)
    for person in range(numOfPeople):
        visited = [False] * numOfPeople
        if dfs(graph, person, 1, visited):
            return 1

    return 0

numOfPeople, numOfEdges = map(int, sys.stdin.readline().split())
infoOfEdges = [list(map(int, sys.stdin.readline().split())) for _ in range(numOfEdges)]

result = solution(numOfPeople, infoOfEdges)
print(result)
