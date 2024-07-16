import sys
from collections import defaultdict, deque

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        cur = queue.popleft()
        for neighbor in relation[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count


# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
trustRelation = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

relation = defaultdict(list)

for end, start in trustRelation:
    relation[start].append(end)

result = []
for i in range(1, N + 1):
    count = bfs(i)
    result.append((i, count))

maxValue = max(result, key=lambda x: x[1])[1]

realResult = [tup for tup in result if tup[1] == maxValue]

for idx, num in realResult:
    print(idx, end=" ")
