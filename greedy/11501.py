import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().strip().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 주식 가격을 확인
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        profit += max_price - price

    print(profit)
