import sys

def solution(given_num, given_list):
    for given in given_list:
        max_gcd = 1
        for r in range(len(given)):
            for c in range(r + 1, len(given)):
                max_gcd = max(max_gcd, gcd(given[r], given[c]))
        print(max_gcd)


def gcd(a, b):
    '''최대 공약수를 구하는 함수
        a, b의 최대 공약수와
        (a - b), b의 최대공약수가 같다는 점을 활용한다.
    '''
    while True:
        if b == 0:  return a

        if a > b:
            a, b = b, a % b
        elif a < b:
            a, b = a, b % a
        else: return a


# 입력값
given_num = int(sys.stdin.readline())
given_list = [list(map(int, sys.stdin.readline().split())) for _ in range(given_num)]

# 풀이
solution(given_num, given_list)

