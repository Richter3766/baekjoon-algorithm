import sys
from collections import deque

def solution(start, target):
    maxLength = 100001
    graph = [-1] * maxLength
    graph[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()

        multipled = cur * 2
        minused = cur - 1
        plused = cur + 1

        if multipled < maxLength and graph[multipled] == -1:
            graph[multipled] = graph[cur]
            queue.append(multipled)

        if 0 <= minused and graph[minused] == -1:
            graph[minused] = graph[cur] + 1
            queue.append(minused)

        if plused < maxLength and graph[plused] == -1:
            graph[plused] = graph[cur] + 1
            queue.append(plused)

        if graph[target] != -1:
            return graph[target]

start, target = map(int, sys.stdin.readline().split())
print(solution(start, target))
