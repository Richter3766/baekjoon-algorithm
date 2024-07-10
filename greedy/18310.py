import sys

N = int(sys.stdin.readline())
locations = list(map(int, sys.stdin.readline().split()))

locations.sort()

antenna = locations[(N - 1) // 2]

print(antenna)