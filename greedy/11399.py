import sys
def solution(N, takenTime):
    takenTime.sort()
    last = 0
    result = 0
    for time in takenTime:
        last += time
        result += last
    return result


N = sys.stdin.readline()
takenTime = list(map(int, sys.stdin.readline().split()))

r = solution(N, takenTime)
print(r)
