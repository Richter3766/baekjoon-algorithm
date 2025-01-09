import sys
import heapq

numOfClasses = int(sys.stdin.readline())
infoOfClasses = [tuple(map(int, sys.stdin.readline().split())) for i in range(numOfClasses)]
infoOfClasses.sort(key=lambda x: x[0])

start, end = infoOfClasses[0]
rooms = []
roomNum = 1
for start, end in infoOfClasses:
    if not rooms:
        heapq.heappush(rooms, (end, start))
        continue

    roomEnd, roomStart = rooms[0]
    if start < roomEnd:
        heapq.heappush(rooms, (end, start))
        roomNum += 1

    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, (end, start))

print(roomNum)