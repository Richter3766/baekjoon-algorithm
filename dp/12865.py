import sys

def findMostValuable(infoOfStuff):
    dp = [0 for i in range(maxWeight + 1)]
    for weight, value in infoOfStuff:
        for i in range(maxWeight, weight - 1, -1):
            dp[i] = max(dp[i] , dp[i - weight] + value)

    return dp[-1]

numOfStuff, maxWeight = map(int, sys.stdin.readline().split())
infoOfStuff = [list(map(int, sys.stdin.readline().split())) for _ in range(numOfStuff)]

result = findMostValuable(infoOfStuff)

print(result)