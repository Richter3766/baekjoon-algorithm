import sys

targetCardsNum = int(sys.stdin.readline())
targetCards = list(map(int, sys.stdin.readline().split()))
randCardsNum = int(sys.stdin.readline())
randCards = list(map(int, sys.stdin.readline().split()))

dicts = {}
for i in targetCards:
    dicts[i] = i

for i in randCards:
    if dicts.get(i) == i:
        print(1, end=" ")
    else:
        print(0, end=" ")