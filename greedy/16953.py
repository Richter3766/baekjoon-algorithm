import sys

def solution(start, target):
    time = 0
    cur = target

    while True:
        time += 1
        if cur == start:
            return time
        elif cur < start:
            return -1

        if cur % 2 == 0:
            cur //= 2
        elif cur % 10 == 1:
            cur //= 10
        else: return -1

start, target = map(int, sys.stdin.readline().split())

result = solution(start, target)
print(result)