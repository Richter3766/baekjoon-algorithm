import sys
import heapq

numOfHomework = int(sys.stdin.readline())
homeworks = [tuple(map(int, sys.stdin.readline().split())) for i in range(numOfHomework)]
homeworks.sort(key=lambda x: (x[0], -x[1]))

primaryQueue = []

for homework in homeworks:
    heapq.heappush(primaryQueue, homework[1])
    if homework[0] < len(primaryQueue):
        heapq.heappop(primaryQueue)

print(sum(primaryQueue))