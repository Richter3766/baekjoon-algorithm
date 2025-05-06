import sys

# 브랜드 정보의 경우
# '(6개 가격, 1개 가격)' 으로 주어짐
# need_string이 되도록하는 최소 가격 찾기

need_string, num_brand = map(int, sys.stdin.readline().split())
brand_info = [list(map(int, sys.stdin.readline().split())) for _ in range(num_brand)]

# 기본 아이디어
# 1. 주어진 브랜드 가격 정보를 세트, 낱개로 각각 오름차순으로 정렬
# 2. 필요한 줄 수가 6개보다 큰 경우
# 낱개로 6개 사거나 세트로 사는 것 중 최솟값으로 계산
# 3. 남은 수의 경우
# 낱개로 사거나 6개 세트로 사는 것 중 최솟값으로 계산

def solution(need_string, num_brand, brand_info):
    answer = 0

    # 정렬
    set_first = sorted(brand_info)
    each_first = sorted(brand_info, key=lambda x: x[1])

    # 세트 수, 남은 줄 수
    set_num, left_num = divmod(need_string, 6)

    # 세트로 사는 경우
    answer += min(set_num * set_first[0][0], each_first[0][1] * set_num * 6)

    # 낱개를 사는 경우
    answer += min(set_first[0][0], left_num * each_first[0][1])

    return answer

answer = solution(need_string, num_brand, brand_info)
print(answer)


def solution_alternative(need_string, num_brand, brand_info):
    """문제를 푸는 어쩌면 더 나은 방식"""
    # 가장 싼 세트 가격과 낱개 가격 찾기
    cheapest_package = min(brand[0] for brand in brand_info)
    cheapest_single = min(brand[1] for brand in brand_info)

    # 세 가지 주요 전략 비용 계산
    # 1. 전부 낱개로 사는 경우
    cost_all_singles = need_string * cheapest_single

    # 2. 필요한 개수를 채우기 위해 전부 세트로 사는 경우 (올림 계산)
    cost_all_sets = ((need_string + 5) // 6) * cheapest_package # (N + 5) // 6 는 ceil(N/6) 계산 트릭

    # 3. 세트 살 만큼 사고 나머지는 낱개로 사는 경우 (몫, 나머지 계산)
    set_num = need_string // 6
    left_num = need_string % 6
    cost_sets_and_singles = set_num * cheapest_package + left_num * cheapest_single

    # 이 세 가지 경우 중 최솟값 반환
    return min(cost_all_singles, cost_all_sets, cost_sets_and_singles)

