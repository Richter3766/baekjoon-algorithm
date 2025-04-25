import sys

def solution(num_list, length):
    cur_list = []

    def backtracking(idx):
        if len(cur_list) == length:
            print(*cur_list)
            return

        for i in range(len(num_list)):
            cur_list.append(num_list[i])
            backtracking(i)
            cur_list.pop()

    for i in range(len(num_list)):
        cur_list.append(num_list[i])
        backtracking(i)
        cur_list.pop()


num, length = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

result = solution(num_list, length)