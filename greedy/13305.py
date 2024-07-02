import sys

N = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

# 최소 비용 계산
min_cost = 0
min_price = prices[0]

for i in range(N - 1):
    min_cost += min_price * distances[i]
    if prices[i + 1] < min_price:
        min_price = prices[i + 1]

print(min_cost)
