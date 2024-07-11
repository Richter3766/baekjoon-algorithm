import sys
from collections import Counter

# 입력 받기
rowNum, colNum = map(int, sys.stdin.readline().split())
lamps = [sys.stdin.readline() for i in range(rowNum)]
clickCount = int(sys.stdin.readline())

# 각 행의 상태와 그 빈도를 계산
counter = Counter(lamps)
maxRowsOn = 0

# 각 행의 상태에 대해 탐색
for rowState, count in counter.items():
    # 해당 행 상태에서 0의 개수를 세기
    zeroCount = rowState.count('0')

    # 해당 행을 모두 켜기 위해 필요한 스위치 클릭 수가 K와 맞는지 확인
    if zeroCount <= clickCount and (clickCount - zeroCount) % 2 == 0:
        # 현재 상태로 모든 램프가 켜진 행의 수를 갱신
        maxRowsOn = max(maxRowsOn, count)

print(maxRowsOn)
