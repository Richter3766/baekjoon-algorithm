import sys

N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

graph = [[0 for i in range(N)] for i in range(N)]
visited = [0] * N
count = 0

def dfs(node):
    visited[node] = 1
    stack = []
    stack.append(node)

    while stack:
        cur = stack.pop()
        for idx in range(N):
            if visited[idx] == 0 and graph[cur][idx] == 1:
                visited[idx] = 1
                stack.append(idx)

for start, end in edges:
    graph[start-1][end-1] = 1
    graph[end-1][start-1] = 1

for node in range(N):
    if visited[node] == 0:
        count += 1
        dfs(node)

print(count)
