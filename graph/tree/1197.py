import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if x_root == y_root:
        return

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for i in range(E)]

edges.sort(key=lambda x:x[2])
parent = [i for i in range(V+1)]
result = 0

for start, end, weight in edges:
    if find(parent, start) != find(parent, end):
        union(parent, start, end)
        result += weight

print(result)
