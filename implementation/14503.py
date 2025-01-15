import sys


def rotate(direction):
    return (direction + 3) % 4

def checkDirection(row, col):
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if room[nr][nc] == 0:
            return True
    return False


rowSize, colSize = map(int, sys.stdin.readline().split())
row, col, direction = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for i in range(rowSize)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cleaned = 0
while True:
    if room[row][col] == 0:
        room[row][col] = 2
        cleaned += 1
    # 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 있는 경우
    if checkDirection(row, col):
        while True:
            # 반시계 방향으로 90도 회전한다.
            direction = rotate(direction)
            dr, dc = directions[direction]
            # 앞쪽 칸이 청소되지 않은 빈 칸인 경우
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if room[row + dr][col + dc] == 0:
                row += dr
                col += dc
                break
    # 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 없는 경우,
    else:
        dr, dc = directions[(direction + 2) % 4]
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if room[row + dr][col + dc] != 1:
            row += dr
            col += dc
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
        else: break

print(cleaned)