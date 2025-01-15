import sys
import heapq

numOfUniversities = int(sys.stdin.readline())

infoUniversities = [tuple(map(int, sys.stdin.readline().split())) for i in range(numOfUniversities)]

infoUniversities.sort(key=lambda x: (x[1], -x[0]))

selections = []
for pay, day in infoUniversities:
    if len(selections) < day:
        heapq.heappush(selections, pay)
    else:
        if selections[0] < pay:
            heapq.heappop(selections)
            heapq.heappush(selections, pay)

print(sum(selections))