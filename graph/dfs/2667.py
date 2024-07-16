import sys


# DFS 함수 정의
def dfs(x, y):
    global count
    # 현재 좌표를 방문 처리하고 count 증가
    visited[y][x] = 1
    count += 1

    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 범위 내에 있고, 아파트가 있으며, 방문하지 않은 경우 DFS 호출
        if 0 <= nx < N and 0 <= ny < N and aparts[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(nx, ny)


# 입력 받기
N = int(sys.stdin.readline().strip())
aparts = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

# 결과를 저장할 리스트
results = []

# 모든 좌표에 대해 DFS 수행
for y in range(N):
    for x in range(N):
        if aparts[y][x] == 1 and visited[y][x] == 0:
            count = 0
            dfs(x, y)
            results.append(count)

# 결과 출력
results.sort()
print(len(results))
for result in results:
    print(result)
