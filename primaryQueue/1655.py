import sys
import heapq

input = sys.stdin.read
data = input().split()
N = int(data[0])
queue = []

left_heap = []  # 최대 힙 (중간값 이하의 값들)
right_heap = []  # 최소 힙 (중간값 이상의 값들)
results = []

for i in range(1, N + 1):
    item = int(data[i])
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -item)
    else:
        heapq.heappush(right_heap, item)

    if right_heap and -left_heap[0] > right_heap[0]:
        left = -heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right)
        heapq.heappush(right_heap, left)

    results.append(-left_heap[0])

for result in results:
    print(result)
