import sys
import heapq

N, times = map(int, sys.stdin.readline().split())
queue = list(map(int, sys.stdin.readline().split()))

heapq.heapify(queue)

for i in range(times):
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)

    first, second = first + second, first + second
    heapq.heappush(queue, first)
    heapq.heappush(queue, second)

result = sum(queue)
print(result)