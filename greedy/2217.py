import sys

N = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(N)]

ropes.sort(reverse=True)

max_weight = 0
for i in range(N):
    max_weight = max(max_weight, (i + 1) * ropes[i])

print(max_weight)
