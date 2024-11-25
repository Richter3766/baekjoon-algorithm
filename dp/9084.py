import sys

def findPossibility(inputs):
    numOfCoins, infoOfCoins, target = inputs
    dp = [0] * (target + 1)
    dp[0] = 1
    for value in infoOfCoins:
        for i in range(value, target + 1):
            dp[i] += dp[i - value]

    return dp[-1]

numOfTC = int(sys.stdin.readline())
inputs = []

for i in range(numOfTC):
    numOfCoins = int(sys.stdin.readline())
    infoOfCoins = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    inputs.append((numOfCoins, infoOfCoins, target))

for i in range(numOfTC):
    result = findPossibility(inputs[i])
    print(result)