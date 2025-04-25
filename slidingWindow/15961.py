import sys
from collections import defaultdict

# 회전 초밥
# 고객은 원하는 초밥을 골라 먹음.
# 초밥은 고유의 숫자로 표현
# 회전 초밥에 같은 초밥이 둘 이상 있을 수 있음.

# 매상 올리기
# 1. 한 지점에서 연속으로 k개 만큼 초밥을 먹으면 할인가로 제공
# 2. 1번에 참가할 경우 특정 초밥을 제공해준다. (벨트에 없어도 반드시 제공)

# 고객은 가능한 한 다양한 초밥을 고른다.

# 임의의 지점에서 다양한 초밥을 먹을 수 있는 경우의 수 찾기

dish_num, dish_num_max, eat_num, coupon_num = map(int, sys.stdin.readline().split())
dish_info = [int(sys.stdin.readline()) for _ in range(dish_num)]

# size eat_num의 윈도우 필요
# 윈도우로 읽으면서 먹을 수 있는 가짓수의 최댓값 갱신


# 처음 윈도우
window = defaultdict(int)
for i in range(eat_num):
    window[dish_info[i]] += 1

max_num = len(window)
if window.get(coupon_num) is None: max_num += 1

for cur in range(1, dish_num):
    # 이전 초밥 빼기
    window[dish_info[cur - 1]] -= 1

    # 다음 초밥 추가
    next_dish = (cur + eat_num - 1) % dish_num
    window[dish_info[next_dish]] += 1

    # 안 먹은 초밥은 삭제
    if window[dish_info[cur - 1]] == 0: del window[dish_info[cur - 1]]

    # 가짓수 최댓값 갱신
    cur_num = len(window)
    if window.get(coupon_num) is None: cur_num += 1 # 아직 쿠폰에 해당하는 초밥을 안먹었으면 추가
    max_num = max(max_num, cur_num)

print(max_num)