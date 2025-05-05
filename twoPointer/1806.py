import sys

length, target = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

def solution(length, target, num_list):
    cur_sum = 0
    left, right = 0, 0
    min_length = float('inf')

    while True:
        if cur_sum < target and right < length:
            cur_sum += num_list[right]
            right += 1
        elif cur_sum >= target:
            min_length = min(min_length, right - left)
            cur_sum -= num_list[left]
            left += 1
        else: break

    return 0 if min_length == float('inf') else min_length

print(solution(length, target, num_list))
