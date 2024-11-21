import sys


def findCases(infoOfCoin, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in infoOfCoin:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[-1]

numOfCoins, target = map(int, sys.stdin.readline().split())
infoOfCoin = [int(sys.stdin.readline()) for _ in range(numOfCoins)]

result = findCases(infoOfCoin, target)
print(result)