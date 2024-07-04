import sys
import heapq

# 입력 처리
N = int(sys.stdin.readline())
assignments = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 마감일을 기준으로 정렬, 같은 마감일이면 점수 높은 순으로 정렬
assignments.sort(key=lambda x: (x[0], -x[1]))
# 우선순위 큐 (최소 힙)
minHeap = []

for deadline, score in assignments:
    heapq.heappush(minHeap, score)
    # 만약 현재 수행한 과제 수가 마감일을 초과하면 점수가 낮은 과제 제거
    if len(minHeap) > deadline:
        heapq.heappop(minHeap)

# 우선순위 큐에 남아 있는 점수들의 합이 최대 점수
print(sum(minHeap))
