import sys

def drawGraph():
    nodesInfo = [[] for i in range(numOfNodes)]
    for start, end in edges:
        nodesInfo[start - 1].append(end)
        nodesInfo[end - 1].append(start)
    return nodesInfo


def findParent(nodesInfo):
    result = [0 for i in range(numOfNodes + 1)]
    visited = [0 for i in range(numOfNodes + 1)]
    stack = [(1, 1)]

    while stack:
        node, parent = stack.pop()
        if visited[node] == 1:
            continue
        visited[node] = 1
        result[node] = parent
        for i in nodesInfo[node - 1]:
            stack.append((i, node))

    return result


def printResult(result):
    for i in result[2:]:
        print(i)

numOfNodes = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for n in range(numOfNodes - 1)]

nodesInfo = drawGraph()
result = findParent(nodesInfo)

printResult(result)