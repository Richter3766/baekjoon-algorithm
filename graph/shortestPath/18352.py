import sys
from collections import deque


def build_graph(city_num, road_info):
    graph = [[] for _ in range(city_num)]
    for start, end in road_info:
        graph[start - 1].append(end - 1)
    return graph


def solution(graph, city_num, target_distance, start_city):
    distance_info = [float('inf')] * city_num
    distance_info[start_city] = 0

    queue = deque([start_city])

    while queue:
        cur_city = queue.popleft()

        for city in graph[cur_city]:
            if distance_info[city] == float('inf'):
                distance_info[city] = distance_info[cur_city] + 1
                queue.append(city)

    return [i for i in range(city_num) if distance_info[i] == target_distance]


city_num, road_num, target_distance, start_city = map(int, sys.stdin.readline().split())
road_info = [list(map(int, sys.stdin.readline().split())) for _ in range(road_num)]

graph = build_graph(city_num, road_info)
result = solution(graph, city_num, target_distance, start_city - 1)

if not result:
    print(-1)
else:
    for i in result:
        print(i + 1)
