import sys

def moveTornado(r, c, dr, dc):
    for i in range(weight):
        if r == 0 and c == 0:
            break
        r, c = r + dr, c + dc
        moveSand(r, c, dr, dc)
    return r, c


def moveSand(r, c, dr, dc):
    global result
    curSand = sandMap[r][c]
    distributions = {
        'down': [(1, 0, 0.07), (1, dc, 0.1), (1, -dc, 0.01), (2, 0, 0.02)],
        'up': [(-1, 0, 0.07), (-1, dc, 0.1), (-1, -dc, 0.01), (-2, 0, 0.02)],
        'right': [(0, 1, 0.07), (dr, 1, 0.1), (-dr, 1, 0.01), (0, 2, 0.02)],
        'left': [(0, -1, 0.07), (dr, -1, 0.1), (-dr, -1, 0.01), (0, -2, 0.02)]
    }
    directions = []

    if abs(dc) == 1:
        directions.extend(distributions['down'])
        directions.extend(distributions['up'])
        directions.extend([(0, 2 * dc, 0.05)])
    elif abs(dr) == 1:
        directions.extend(distributions['right'])
        directions.extend(distributions['left'])
        directions.extend([(2 * dr, 0, 0.05)])

    movedSand = 0
    for d in directions:
        drOffset, dcOffset, ratio = d
        nr = r + drOffset
        nc = c + dcOffset
        amount = int(curSand * ratio)
        movedSand += amount
        # 맵의 범위를 체크하고 모래를 분배
        if 0 <= nr < sizeN and 0 <= nc < sizeN:
            sandMap[nr][nc] += amount
        else:
            result += amount

    if abs(dr) == 1:
        if 0 <= r + dr < sizeN:
            sandMap[r + dr][c] += curSand - movedSand
        else:
            result += curSand - movedSand
    elif abs(dc) == 1:
        if 0 <= c + dc < sizeN:
            sandMap[r][c + dc] += curSand - movedSand
        else:
            result += curSand - movedSand
    sandMap[r][c] = 0
# 토네이도가 움직이는 방향을 담은 반복문 필요
# 각 반복마다 토네이도 이동으로 인해 날라가는 모래의 양 계산 필요
# 움직이는 모래의 방향과 양은 토네이도가 이동한 그 지점에서 계산하면 됨.
# 격자 밖으로 모래가 나갈 때마다 결과값에 + 해주면 된다.

sizeN = int(sys.stdin.readline())
sandMap = [list(map(int, sys.stdin.readline().split())) for i in range(sizeN)]
center = sizeN // 2

# 토네이도 이동 방향 순서 -> 좌 하 우 상
# 이동 거리는 1부터 시작해서 두 번 이동 후 1씩 증가
# 시작 위치는 격자의 중앙
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
directionIdx = 0
weight = 1
iterIdx = 0
r, c = center, center
result = 0
while True:
    if r == 0 and c == 0:
        break
    dr, dc = directions[directionIdx % 4]

    r, c = moveTornado(r, c, dr, dc)
    iterIdx += 1
    directionIdx += 1

    if iterIdx % 2 == 0:
        weight += 1

print(result)
