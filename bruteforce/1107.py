import sys
from itertools import product

def solution(target_channel, info_broken):
    # 현재 채널은 100
    cur = 100

    # 고장나지 않은 버튼 목록
    button = [i for i in range(10) if i not in info_broken]

    # 1. +, - 버튼으로만 움직였을 경우
    only_updown = abs(target_channel - cur)

    # 2. 고장나지 않은 숫자 버튼으로 목표에 가장 가까운 숫자 만들기
    closest_num = find_closest_num(target_channel, button)

    # 3. 두 경우의 최소값 반환
    return min(only_updown, closest_num)


def find_closest_num(target_channel, button):
    closest_num = None
    min_presses = float('inf')

    # 가능한 모든 조합을 탐색
    for length in range(1, 7):
        for comb in product(button, repeat=length):
            num = int(''.join(map(str, comb)))
            presses = abs(target_channel - num) + length
            if presses < min_presses:
                min_presses = presses
                closest_num = num

    return min_presses


target_channel = int(sys.stdin.readline())
num_broken = int(sys.stdin.readline())
info_broken = list(map(int, sys.stdin.readline().split())) if num_broken != 0 else []

result = solution(target_channel, info_broken)
print(result)
