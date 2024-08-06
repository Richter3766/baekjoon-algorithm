import sys
from collections import deque

cols, rows = map(int, sys.stdin.readline().split())
tomatoMap = []
ripeTomatoes = deque()
unripeTomatoes = deque()

# 1은 '익은' 토마토
# 0은 '안 익은' 토마토
# -1은 비어 있는 칸
# 익은 토마토 기준 상하좌우가 익게 됨
# 안 익은 토마토는 결코 스스로 익지 않음
# 비어있다면 그 너머에 있는 토마토는 결코 익을 수 없다

# 입력을 받을 때 익은 토마토의 위치를 리스트로 담기
for i in range(rows):
    row = list(map(int, sys.stdin.readline().split()))
    tomatoMap.append(row)
    for idx, j in enumerate(row):
        if j == 1:
            ripeTomatoes.append((i, idx, 0))
        elif j == 0:
            unripeTomatoes.append((i, idx))

# 처음부터 모두 익어있으면 0
if not unripeTomatoes:
    print(0)
    exit(0)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 익은 토마토를 큐에 넣고 BFS 탐색 -> 0을 만나면 1 변경 후 해당 위치 큐에 넣기
while ripeTomatoes:
    row, col, day = ripeTomatoes.popleft()
    for drow, dcol in directions:
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < rows and 0 <= ncol < cols and tomatoMap[nrow][ncol] == 0:
            tomatoMap[nrow][ncol] = day + 1
            ripeTomatoes.append((nrow, ncol, day + 1))

result = 0
canAllRipe = True
for i in range(rows):
    for j in range(cols):
        if tomatoMap[i][j] == 0:
            canAllRipe = False
            break
        result = max(result, tomatoMap[i][j])
    if not canAllRipe:
        break

# 모두 익으면 익은 날짜
# 불가능하면 -1
if not canAllRipe:
    print(-1)
else:
    print(result)
