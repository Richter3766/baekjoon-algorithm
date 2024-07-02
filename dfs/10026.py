import sys

def dfs(x, y, color, visited, check_color):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and check_color(colors[ny][nx], color):
                stack.append((nx, ny))

def normal_check(c1, c2):
    return c1 == c2

def abnormal_check(c1, c2):
    return (c1 in 'RG' and c2 in 'RG') or c1 == c2

# 입력 받기
N = int(sys.stdin.readline().strip())
colors = [list(sys.stdin.readline().strip()) for _ in range(N)]

visitedNormal = [[0] * N for _ in range(N)]
visitedAbnormal = [[0] * N for _ in range(N)]

normalCount = 0
abnormalCount = 0

for y in range(N):
    for x in range(N):
        if not visitedNormal[y][x]:
            dfs(x, y, colors[y][x], visitedNormal, normal_check)
            normalCount += 1
        if not visitedAbnormal[y][x]:
            dfs(x, y, colors[y][x], visitedAbnormal, abnormal_check)
            abnormalCount += 1

print(normalCount, abnormalCount)
