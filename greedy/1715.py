import sys
import heapq

# 입력 받기
N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]

# 최소 힙 만들기
heapq.heapify(cards)

total_comparisons = 0

# 힙에서 두 개의 가장 작은 요소를 계속해서 꺼내 합친 뒤 다시 힙에 넣는 과정을 반복
# 이는 카드를 합칠 때 전체에서 가장 작은 카드 뭉치 두 개를 고르기 위함이다.
while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    combined = first + second
    total_comparisons += combined
    heapq.heappush(cards, combined)

# 결과 출력
print(total_comparisons)
