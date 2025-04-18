import sys

def solution(target_num, city_info):
    # 도시 정보는 cost, num으로
    # cost만큼 썼을 때 num만큼 고객 수 모집
    # 최소한의 cost로 target_num 이상의 고객 수 모집하기

    # 도시 정보를 정렬하여
    # 최대 비용으로 1명만 모집가능할 때
    # 필요한 비용을 상한값으로 잡기
    city_info.sort()
    max_range = city_info[-1][0] * target_num + 1 # 최악의 경우를 상정함
    dp_table = [0] * max_range

    # 처음 도시 정보로 dp_table 초기화
    for cost, num in city_info:
        dp_table[cost] = max(dp_table[cost], num)

    # 최대 범위만큼 서치
    for cost in range(1, max_range + 1):
        for city_cost, city_num in city_info:
            if city_cost <= cost:
                dp_table[cost] = max(dp_table[cost], city_num + dp_table[cost - city_cost])

        if dp_table[cost] >= target_num:
            return cost


target_num, city_num = map(int, sys.stdin.readline().split())
city_info = [list(map(int, sys.stdin.readline().split())) for _ in range(city_num)]

answer = solution(target_num, city_info)
print(answer)