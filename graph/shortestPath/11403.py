import sys

numOfVertex = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for i in range(numOfVertex)]

for k in range(numOfVertex):
    for r in range(numOfVertex):
        for c in range(numOfVertex):
            if edges[r][k] == 1 and edges[k][c] == 1:
                edges[r][c] = 1

for r in range(numOfVertex):
    for c in range(numOfVertex):
        print(edges[r][c], end=" ")
    print()