import sys

N = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

arrA.sort()
arrB.sort(reverse=True)

result = 0

for i in range(N):
    result += arrA[i] * arrB[i]

print(result)