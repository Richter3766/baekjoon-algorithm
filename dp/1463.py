import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
queue.append((N, 0))
visited = set()  # 방문한 숫자를 기록하기 위한 집합
visited.add(N)

while queue:
    current, depth = queue.popleft()

    if current == 1:
        print(depth)
        break

    # 3으로 나누어 떨어질 때
    if current % 3 == 0 and (current // 3) not in visited:
        queue.append((current // 3, depth + 1))
        visited.add(current // 3)

    # 2로 나누어 떨어질 때
    if current % 2 == 0 and (current // 2) not in visited:
        queue.append((current // 2, depth + 1))
        visited.add(current // 2)

    # 1을 뺄 때
    if (current - 1) not in visited:
        queue.append((current - 1, depth + 1))
        visited.add(current - 1)
