import sys

def findMinimumCoins(numOfCoins, infoOfCoins, target):
    limit = float('inf')
    dp = [limit] * (target + 1)

    for value in infoOfCoins:
        for i in range(value, target + 1):
            if i % value == 0:
                dp[i] = min(dp[i], i // value)
            if dp[i - value] != limit:
                dp[i] = min(dp[i], dp[i - value] + 1)
    if dp[-1] == limit:
        return -1
    return dp[-1]

numOfCoins, target = map(int, sys.stdin.readline().split())
infoOfCoins = [int(sys.stdin.readline()) for _ in range(numOfCoins)]

result = findMinimumCoins(numOfCoins, infoOfCoins, target)

print(result)