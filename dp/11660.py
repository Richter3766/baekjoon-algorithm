import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
coordinates = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

prefixSum = [[0 for i in range(N + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefixSum[i][j] = matrix[i - 1][j - 1] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]

for sx, sy, ex, ey in coordinates:
    result = prefixSum[ex][ey] - prefixSum[ex][sy - 1] - prefixSum[sx -1][ey] + prefixSum[sx -1][sy - 1]
    print(result)