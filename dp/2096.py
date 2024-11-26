import sys


numOfLines = int(sys.stdin.readline())

dpMax = [0] * 3
dpMin = [0] * 3

for i in range(numOfLines):
    curLine = list(map(int, sys.stdin.readline().split()))
    dpMax = [curLine[0] + max(dpMax[:2]), curLine[1] + max(dpMax), curLine[2] + max(dpMax[1:])]
    dpMin = [curLine[0] + min(dpMin[:2]), curLine[1] + min(dpMin), curLine[2] + min(dpMin[1:])]

print(max(dpMax), min(dpMin))