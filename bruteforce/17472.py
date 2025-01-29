import sys
from collections import deque
import heapq


def find_island(world_map):
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    island_map = []
    for r in range(row_size):
        for c in range(col_size):
            if world_map[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                island_node = bfs(world_map, r, c, visited)
                island_map.append(island_node)

    return island_map


def bfs(world_map, r, c, visited):
    directinos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    node = [(r, c)]
    queue = deque()
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directinos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row_size and 0 <= nc < col_size and world_map[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                node.append((nr, nc))
                queue.append((nr, nc))

    return node


def build_graph(world_map, island_map):
    graph = [[] for i in range(len(island_map))]

    for idx in range(len(island_map)):
        for r, c in island_map[idx]:
            left, right = find_col(r, c, world_map, -1), find_col(r, c, world_map, 1)
            top, bottom = find_row(r, c, world_map, -1), find_row(r, c, world_map, 1)

            if left is not None: build_bridge(left, graph, island_map, idx)
            if right is not None: build_bridge(right, graph, island_map, idx)
            if top is not None: build_bridge(top, graph, island_map, idx)
            if bottom is not None: build_bridge(bottom, graph, island_map, idx)

    return graph


def build_bridge(point, graph, island_map, idx):
    r, c, length = point

    for i in range(len(island_map)):
        if (r, c) in island_map[i]:
            graph[idx].append((length, i))
            return graph

def find_row(r, c, world_map, dr):
    length = 0
    cur = r
    while True:
        cur += dr
        if cur < 0 or cur >= row_size:
            return None
        if world_map[cur][c] == 1:
            break
        length += 1

    if length >= 2:
        return (cur, c, length)
    return None


def find_col(r, c, world_map, dc):
    length = 0
    cur = c
    while True:
        cur += dc
        if cur < 0 or cur >= col_size:
            return None

        if world_map[r][cur] == 1:
            break
        length += 1

    if length >= 2:
        return (r, cur, length)
    return None


def build_mst(graph):
    min_heap = [(0, 0)]
    visited = [False for i in range(len(graph))]
    result = 0
    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if not visited[node]:
            visited[node] = True
            result += weight

            for adjusted_weight, adjusted_node in graph[node]:
                heapq.heappush(min_heap, (adjusted_weight, adjusted_node))
    if all(visit for visit in visited):
        return result
    return -1


row_size, col_size = map(int, sys.stdin.readline().split())
world_map = [list(map(int, sys.stdin.readline().split())) for i in range(row_size)]

# BFS로 섬을 찾고 노드로 저장하기
island_map = find_island(world_map)

# 각 섬끼리 연결 가능한 모든 다리 생성하기
graph = build_graph(world_map, island_map)

# 모든 섬간 이동이 가능한지 확인
if not all(node for node in graph):
    print(-1)
else: # 가능하면
    # 프림 알고리즘으로 MST 생성하기
    result = build_mst(graph)
    if result == 0: print(-1)
    # 그때의 가중치 합이 최소가 될 것
    else: print(result)


