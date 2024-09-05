import sys
from collections import defaultdict

def topologicalSort(n, comparisons):
    # 그래프 생성
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for a, b in comparisons:
        graph[a].append(b)
        in_degree[b] += 1

    # 토폴로지 정렬
    queue = [node for node in range(1, n + 1) if in_degree[node] == 0]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 결과 반환
    return result if len(result) == n else []

# 입력 예시
N, M = map(int, sys.stdin.readline().split())
comparisons = [tuple(map(int, sys.stdin.readline().split())) for i in range(M)]
for i in topologicalSort(N, comparisons):
    print(i, end=" ")