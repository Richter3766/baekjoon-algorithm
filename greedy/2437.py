import sys

numOfWeights = int(sys.stdin.readline())
infoOfWeights = list(map(int, sys.stdin.readline().split()))
infoOfWeights.sort()

numRange = 0
for weight in infoOfWeights:
    if numRange + 1 < weight:
        break

    numRange += weight

print(numRange + 1)