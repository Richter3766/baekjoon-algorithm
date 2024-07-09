import sys
import heapq

queue = []
N = int(sys.stdin.readline())

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))

    for item in row:
        if len(queue) < N:
            heapq.heappush(queue, item)
        else:
            heapq.heappushpop(queue, item)

result = heapq.heappop(queue)

print(result)