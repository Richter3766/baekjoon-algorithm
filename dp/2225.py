import sys

target,  num = map(int, sys.stdin.readline().split())

dp = [[0 for i in range(target + 1)] for i in range(num + 1)]

for i in range(target + 1):
    dp[1][i] = 1

for k in range(1, num + 1):
    for i in range(target + 1):
        for j in range(i + 1):
            dp[k][i] += dp[k - 1][i - j]

print(dp[-1][-1] % 1000000000)